library(fs)
library(tidyverse)
library(arrow)

urls <- c("https://raw.githubusercontent.com/CDCgov/covid19-forecast-hub/refs/heads/main/model-output/CFA_Pyrenew-Pyrenew_H_COVID/2025-04-05-CFA_Pyrenew-Pyrenew_H_COVID.csv",
"https://raw.githubusercontent.com/CDCgov/covid19-forecast-hub/refs/heads/main/model-output/CFA_Pyrenew-Pyrenew_HW_COVID/2025-04-05-CFA_Pyrenew-Pyrenew_HW_COVID.csv",
"https://raw.githubusercontent.com/CDCgov/covid19-forecast-hub/refs/heads/main/model-output/CFA_Pyrenew-Pyrenew_HE_COVID/2025-04-05-CFA_Pyrenew-Pyrenew_HE_COVID.csv")

super_mega_hubverse <-
  tibble(url = urls) |>
  mutate(data = url |> map(read_csv)) |>
  mutate(model = url |> path_dir() |> path_file()) |>
  select(model, data) |>
  unnest("data")
write_parquet(
    super_mega_hubverse,
    "super_mega_hubverse_example.parquet")
