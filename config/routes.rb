Rails.application.routes.draw do

  get 'flex_only' => 'responsive_design#flex_only'
  get 'media_only' => 'responsive_design#media_only'
  root 'responsive_design#overview'

end
