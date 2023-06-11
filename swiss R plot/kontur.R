library(sf)
library(tidyverse)
library(rayshader)
library(rayrender)
library(stars)
library(MetBrewer)
library(colorspace)
#library(rgl)
#library(devtools)

#install.packages("rgl")

#install_github("tylermorganwall/rayshader")
#install_github("tylermorganwall/rayrender")

# load kontur data (switzerland only)
data <- st_read("../data/map/swiss_border/kontur_population_CH_20220630.gpkg")

# load swiss map
map <- st_read("../data/map/swiss_border/switzerland-detailed-boundary_1043.geojson") |>
  st_transform(st_crs(data))


# plot map
map |>
  ggplot() +
  geom_sf()

st_ch <- st_intersection(data, map)

# create bounding box for our data
bb <- st_bbox(st_ch)

# create points
bottom_left <- st_point(c(bb[["xmin"]], bb[["ymin"]])) |>
  st_sfc(crs = st_crs(data))

bottom_right <- st_point(c(bb[["xmax"]], bb[["ymin"]])) |>
  st_sfc(crs = st_crs(data))

top_left <- st_point(c(bb[["xmin"]], bb[["ymax"]])) |>
  st_sfc(crs = st_crs(data))

# add point to plot
map |>
  ggplot() +
  geom_sf() +
  geom_sf(data = bottom_left) + 
  geom_sf(data = bottom_right) + 
  geom_sf(data = top_left)

# compute distances 
width <- st_distance(bottom_left, bottom_right)
height <- st_distance(bottom_left, top_left)

# compute ratio
if (width > height) {
  w_ratio <- 1
  h_ratio <- height/width
} else {
  w_ratio <- width/height
  h_ratio <- 1
}

# convert to raster so we can then convert to matrix
size <- 1000 # base <- set to 1000 for tests
x <- floor(size * w_ratio)
y <- floor(size * h_ratio)
map_rast <- st_rasterize(st_ch,
                         nx = x,
                         ny = y)

# convert to matrix
mat <- matrix(map_rast$population,
              nrow = x,
              ncol = y)

# create color palette

c1 <- met.brewer("OKeeffe2")
swatchplot(c1)

texture <- grDevices::colorRampPalette(c1, bias = 3)(256)
swatchplot(texture)

# plot
mat |>
  height_shade(texture = texture) |>
  rayshader::plot_3d(heightmap = mat,
          zscale = 150,
          solid = FALSE,
          shadowdepth = 0)

# change camera angle
render_camera(theta = 25, phi = 45, zoom = 0.85)

#render high quality image
render_highquality(
  filename = "images/final_plot.png",
  interactive = FALSE,
  lightdirection = 120,
  lightaltitude = c(20, 80), # 2 lights
  lightcolor = c(c1[2], "white"),
  lightintensity = c(600, 300),
  # remove next values to test
  samples = 100,
  width = 2000,
  height = 2000
)




