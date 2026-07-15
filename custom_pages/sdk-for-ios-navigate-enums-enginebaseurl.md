---
title: "EngineBaseURL Enumeration Reference"
slug: "sdk-for-ios-navigate-enums-enginebaseurl"
---

# EngineBaseURL

<div class="declaration">

<div class="language">

``` highlight
public enum EngineBaseURL : UInt32, CaseIterable, Codable
```

</div>

</div>

Lists the available HERE SDK endpoints that can be customized with a custom backend base URL.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk13EngineBaseURLO06searchB0yA2CmF"></span>` `<span id="//apple_ref/swift/Element/searchEngine" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-enums-enginebaseurl#/s:7heresdk13EngineBaseURLO06searchB0yA2CmF" class="token"><code>searchEngine</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates a <a href="sdk-for-ios-navigate-classes-searchengine">`SearchEngine`</a> endpoint. Note that the provided string value will replace the base URL. The endpoint names for this engine are “v1/discover”, “v1/geocode”, “v1/revgeocode”, “v1/autosuggest”, “v1/lookup” and “v1/browse”. A valid base string value could look like “<a href="http://www.my-company.com">www.my-company.com</a>”. An example of the resulting URL for the first endpoint looks like this: “<https://www.my-company.com/v1/discover>” appended with query data. You need to ensure that the provided base URL supports all required endpoints.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case searchEngine
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13EngineBaseURLO07routingB0yA2CmF"></span>` `<span id="//apple_ref/swift/Element/routingEngine" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-enums-enginebaseurl#/s:7heresdk13EngineBaseURLO07routingB0yA2CmF" class="token"><code>routingEngine</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates a <a href="sdk-for-ios-navigate-classes-routingengine">`RoutingEngine`</a> endpoint. Note that the provided string value will replace the base URL. The endpoint names for this engine are “v8/routes”, “v8/import”. A valid base string value could look like “<a href="http://www.my-company.com">www.my-company.com</a>”. An example of the resulting URL for the first endpoint looks like this: “<https://www.my-company.com/v8/routes>” appended with query data. You need to ensure that the provided base URL supports all required endpoints.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case routingEngine
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13EngineBaseURLO14authenticationyA2CmF"></span>` `<span id="//apple_ref/swift/Element/authentication" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-enums-enginebaseurl#/s:7heresdk13EngineBaseURLO14authenticationyA2CmF" class="token"><code>authentication</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates base url for <a href="sdk-for-ios-navigate-classes-authentication">`Authentication`</a>. Note that the provided string value will replace the base URL. The endpoint name for this base url is “oauth2/token”. A valid base string value could look like “<a href="http://www.my-company.com">www.my-company.com</a>”. An example of the resulting URL for the endpoint looks like this: “<https://www.my-company.com/oauth2/token>” appended with query data. You need to ensure that the provided base URL supports required endpoint.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case authentication
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13EngineBaseURLO7dsProxyyA2CmF"></span>` `<span id="//apple_ref/swift/Element/dsProxy" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-enums-enginebaseurl#/s:7heresdk13EngineBaseURLO7dsProxyyA2CmF" class="token"><code>dsProxy</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies the endpoint URL for a map catalog. This is only relevant for the Navigate license that uses OCM based map data when a custom catalog configuration should be loaded. By default, the data Service proxy, in short `EngineBaseURL.dsProxy`, is set to “<https://direct.data.api.platform.here.com/direct/v1>”. When a custom catalog should be used, then the HERE SDK will internally do a lookup request to find out which URL to use to access catalog. In order to bypass this extra request, we recommend to set the URL upfront when initializing the HERE SDK. For example, a valid `EngineBaseURL.dsProxy` for a custom catalog may look like this: “<https://data.api.platform.yourcompany.com/direct/v1>”. Note that this is not a network proxy setting. If you do not load a custom catalog configuration, you can ignore this setting.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case dsProxy
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13EngineBaseURLO11trafficDatayA2CmF"></span>` `<span id="//apple_ref/swift/Element/trafficData" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-enums-enginebaseurl#/s:7heresdk13EngineBaseURLO11trafficDatayA2CmF" class="token"><code>trafficData</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates a `Traffic Data` endpoint. Note that the provided string value will replace the base URL. This is only relevant for TrafficEngine. For traffic incident and flow presented in the map view, please use <a href="sdk-for-ios-navigate-enums-enginebaseurl#/s:7heresdk13EngineBaseURLO24trafficVectorTileServiceyA2CmF">`EngineBaseURL.trafficVectorTileService`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case trafficData
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13EngineBaseURLO24trafficVectorTileServiceyA2CmF"></span>` `<span id="//apple_ref/swift/Element/trafficVectorTileService" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-enums-enginebaseurl#/s:7heresdk13EngineBaseURLO24trafficVectorTileServiceyA2CmF" class="token"><code>trafficVectorTileService</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates a `Traffic Vector Tile API` endpoint. Note that the provided string value will replace the base URL. This is only relevant for traffic presented in the map view. For the TrafficEngine, please use <a href="sdk-for-ios-navigate-enums-enginebaseurl#/s:7heresdk13EngineBaseURLO11trafficDatayA2CmF">`EngineBaseURL.trafficData`</a>.

  The service needs to comply with <https://www.here.com/docs/bundle/traffic-vector-tile-api-v2-api-reference/page/index.html> The endpoint name for this engine is “v2/traffictiles”. A valid base string value could look like “<a href="http://www.my-company.com">www.my-company.com</a>”. The resulting URL looks like this: “<https://www.my-company.com/v2/traffictiles/%7Blayer%7D/mc/%7Bz%7D/%7Bx%7D/%7By%7D/omv>”, with concrete tile IDs in {x}, {y}, {z} and {layers} in (flow, incidents). You need to ensure that the provided base URL supports all required endpoints.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case trafficVectorTileService
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13EngineBaseURLO17rasterTileServiceyA2CmF"></span>` `<span id="//apple_ref/swift/Element/rasterTileService" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-enums-enginebaseurl#/s:7heresdk13EngineBaseURLO17rasterTileServiceyA2CmF" class="token"><code>rasterTileService</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates a `Raster Tile API` endpoint. Note that the provided string value will replace the URL template. A valid URL template value could look like: “<https://www.my-company.com/satellite.day/%7Bz%7D/%7Bx%7D/%7By%7D/512/jpg>”

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case rasterTileService
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13EngineBaseURLO014isolineRoutingB0yA2CmF"></span>` `<span id="//apple_ref/swift/Element/isolineRoutingEngine" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-enums-enginebaseurl#/s:7heresdk13EngineBaseURLO014isolineRoutingB0yA2CmF" class="token"><code>isolineRoutingEngine</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates a <a href="sdk-for-ios-navigate-classes-isolineroutingengine">`IsolineRoutingEngine`</a> endpoint. Note that the provided string value will replace the base URL. The endpoint names for this engine are “v8/isolines”. A valid base string value could look like “<a href="http://www.my-company.com">www.my-company.com</a>”. An example of the resulting URL for the first endpoint looks like this: “<https://www.my-company.com/v8/isolines>” appended with query data. You need to ensure that the provided base URL supports all required endpoints.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case isolineRoutingEngine
  ```

  </div>

  </div>

  </div>

  </div>

</div>

</div>

</div>

<div id="sdk-for-ios-navigate-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

