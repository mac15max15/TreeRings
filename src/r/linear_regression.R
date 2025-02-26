


rm(list=ls())

setwd('/Users/maxcaragozian/Desktop/BIOL 470/trees/src/r')
data_path <- "/Users/maxcaragozian/Desktop/BIOL 470/trees/aggregated_data/"



socal_data <- read.csv(paste(data_path, 'SOCAL.csv', sep=''))
socal_ols <- lm(
  socal_data$avg_ring_width ~ 
    socal_data$scaled_rainfall + 
    socal_data$scaled_temp +
    socal_data$scaled_rainfall_lag1
    )

summary(socal_ols)

sierra_data <- read.csv(paste(data_path, 'SIERRA.csv', sep=''))
sierra_ols <- lm(
  sierra_data$avg_ring_width ~ 
    sierra_data$scaled_rainfall + 
    sierra_data$scaled_temp +
    sierra_data$scaled_rainfall_lag1
)

summary(sierra_ols)

colo_data <- read.csv(paste(data_path, 'COLO.csv', sep=''))
colo_ols <- lm(
  colo_data$avg_ring_width ~ 
    colo_data$scaled_rainfall + 
    colo_data$scaled_temp +
    colo_data$scaled_rainfall_lag1
)

summary(colo_ols)
