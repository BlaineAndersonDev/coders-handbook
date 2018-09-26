Rails.application.routes.draw do

  get 'flex_only' => 'responsive_design#flex_only'
  get 'media_only' => 'responsive_design#media_only'
  get 'flex_media' => 'responsive_design#flex_media'
  get 'overview' => 'responsive_design#overview'

  get 'welcome' => 'welcome#welcome'
  root 'welcome#welcome'

end
