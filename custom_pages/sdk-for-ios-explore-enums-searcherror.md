---
title: "SearchError Enumeration Reference"
slug: "sdk-for-ios-explore-enums-searcherror"
---

# SearchError

<div class="declaration">

<div class="language">

``` highlight
public enum SearchError : UInt32, CaseIterable, Codable
```

</div>

</div>

Specifies possible errors that may result from a search query.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11SearchErrorO20authenticationFailedyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-authenticationFailed" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-searcherror#sdk-for-ios-explore-s-7heresdk11SearchErrorO20authenticationFailedyA2CmF" class="token"><code>authenticationFailed</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Search operation is not authenticated. Check your credentials.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case authenticationFailed = 1
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11SearchErrorO18maxItemsOutOfRangeyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-maxItemsOutOfRange" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-searcherror#sdk-for-ios-explore-s-7heresdk11SearchErrorO18maxItemsOutOfRangeyA2CmF" class="token"><code>maxItemsOutOfRange</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Should be in the range \[1, 100\].

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case maxItemsOutOfRange
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11SearchErrorO07parsingC0yA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-parsingError" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-searcherror#sdk-for-ios-explore-s-7heresdk11SearchErrorO07parsingC0yA2CmF" class="token"><code>parsingError</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Error while parsing response data.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case parsingError
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11SearchErrorO14noResultsFoundyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-noResultsFound" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-searcherror#sdk-for-ios-explore-s-7heresdk11SearchErrorO14noResultsFoundyA2CmF" class="token"><code>noResultsFound</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  No results found.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case noResultsFound
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11SearchErrorO04httpC0yA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-httpError" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-searcherror#sdk-for-ios-explore-s-7heresdk11SearchErrorO04httpC0yA2CmF" class="token"><code>httpError</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Network request error.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case httpError
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11SearchErrorO17serverUnreachableyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-serverUnreachable" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-searcherror#sdk-for-ios-explore-s-7heresdk11SearchErrorO17serverUnreachableyA2CmF" class="token"><code>serverUnreachable</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Server unreachable.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case serverUnreachable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11SearchErrorO9forbiddenyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-forbidden" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-searcherror#sdk-for-ios-explore-s-7heresdk11SearchErrorO9forbiddenyA2CmF" class="token"><code>forbidden</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The credentials given do not provide access to the resource requested.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case forbidden
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11SearchErrorO18exceededUsageLimityA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-exceededUsageLimit" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-searcherror#sdk-for-ios-explore-s-7heresdk11SearchErrorO18exceededUsageLimityA2CmF" class="token"><code>exceededUsageLimit</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Credentials exceeded the allowed requests limit.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case exceededUsageLimit
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11SearchErrorO15operationFailedyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-operationFailed" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-searcherror#sdk-for-ios-explore-s-7heresdk11SearchErrorO15operationFailedyA2CmF" class="token"><code>operationFailed</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Operation failed due to an internal error.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case operationFailed
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11SearchErrorO18operationCancelledyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-operationCancelled" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-searcherror#sdk-for-ios-explore-s-7heresdk11SearchErrorO18operationCancelledyA2CmF" class="token"><code>operationCancelled</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Operation cancelled.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case operationCancelled
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11SearchErrorO8timedOutyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-timedOut" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-searcherror#sdk-for-ios-explore-s-7heresdk11SearchErrorO8timedOutyA2CmF" class="token"><code>timedOut</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The request timed out.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case timedOut
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11SearchErrorO7offlineyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-offline" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-searcherror#sdk-for-ios-explore-s-7heresdk11SearchErrorO7offlineyA2CmF" class="token"><code>offline</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The device does not have an internet connection.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case offline
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11SearchErrorO12queryTooLongyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-queryTooLong" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-searcherror#sdk-for-ios-explore-s-7heresdk11SearchErrorO12queryTooLongyA2CmF" class="token"><code>queryTooLong</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Query is too long, max. size is 300 characters.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case queryTooLong
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11SearchErrorO13filterTooLongyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-filterTooLong" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-searcherror#sdk-for-ios-explore-s-7heresdk11SearchErrorO13filterTooLongyA2CmF" class="token"><code>filterTooLong</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Filter is too long, max. size is 300 characters.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case filterTooLong
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11SearchErrorO25proxyAuthenticationFailedyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-proxyAuthenticationFailed" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-searcherror#sdk-for-ios-explore-s-7heresdk11SearchErrorO25proxyAuthenticationFailedyA2CmF" class="token"><code>proxyAuthenticationFailed</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Proxy is not authenticated. Check your proxy credentials.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case proxyAuthenticationFailed
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11SearchErrorO22proxyServerUnreachableyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-proxyServerUnreachable" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-searcherror#sdk-for-ios-explore-s-7heresdk11SearchErrorO22proxyServerUnreachableyA2CmF" class="token"><code>proxyServerUnreachable</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Proxy server unreachable.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case proxyServerUnreachable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11SearchErrorO10queryEmptyyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-queryEmpty" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-searcherror#sdk-for-ios-explore-s-7heresdk11SearchErrorO10queryEmptyyA2CmF" class="token"><code>queryEmpty</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Empty query

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case queryEmpty
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11SearchErrorO11invalidAreayA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-invalidArea" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-searcherror#sdk-for-ios-explore-s-7heresdk11SearchErrorO11invalidAreayA2CmF" class="token"><code>invalidArea</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Box or circle area of query is invalid

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case invalidArea
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11SearchErrorO11filterEmptyyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-filterEmpty" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-searcherror#sdk-for-ios-explore-s-7heresdk11SearchErrorO11filterEmptyyA2CmF" class="token"><code>filterEmpty</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Filter is empty

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case filterEmpty
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11SearchErrorO23invalidCorridorPolylineyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-invalidCorridorPolyline" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-searcherror#sdk-for-ios-explore-s-7heresdk11SearchErrorO23invalidCorridorPolylineyA2CmF" class="token"><code>invalidCorridorPolyline</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Corridor area polyline size is less than 2 points

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case invalidCorridorPolyline
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11SearchErrorO10invalidUrlyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-invalidUrl" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-searcherror#sdk-for-ios-explore-s-7heresdk11SearchErrorO10invalidUrlyA2CmF" class="token"><code>invalidUrl</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Url is invalid

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case invalidUrl
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11SearchErrorO25invalidCustomOptionFormatyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-invalidCustomOptionFormat" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-searcherror#sdk-for-ios-explore-s-7heresdk11SearchErrorO25invalidCustomOptionFormatyA2CmF" class="token"><code>invalidCustomOptionFormat</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Custom options are set in an invalid format in the query

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case invalidCustomOptionFormat
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11SearchErrorO17invalidTruckClassyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-invalidTruckClass" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-searcherror#sdk-for-ios-explore-s-7heresdk11SearchErrorO17invalidTruckClassyA2CmF" class="token"><code>invalidTruckClass</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Light truck class is passed in the filter

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case invalidTruckClass
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11SearchErrorO10badRequestyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-badRequest" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-searcherror#sdk-for-ios-explore-s-7heresdk11SearchErrorO10badRequestyA2CmF" class="token"><code>badRequest</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Bad network request

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case badRequest
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11SearchErrorO11mapNotReadyyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-mapNotReady" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-searcherror#sdk-for-ios-explore-s-7heresdk11SearchErrorO11mapNotReadyyA2CmF" class="token"><code>mapNotReady</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Offline map data is incomplete for the requested operation. Regions are not downloaded or are in the `Pending` state.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case mapNotReady
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11SearchErrorO19layersNotDownloadedyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-layersNotDownloaded" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-searcherror#sdk-for-ios-explore-s-7heresdk11SearchErrorO19layersNotDownloadedyA2CmF" class="token"><code>layersNotDownloaded</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Downloaded regions missing <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#sdk-for-ios-explore-s-7heresdk18LayerConfigurationV7FeatureO19offlineSearchGlobalyA2EmF">`LayerConfiguration.Feature.offlineSearchGlobal`</a> feature. Update or redownload regions with enabled feature.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case layersNotDownloaded
  ```

  </div>

  </div>

  </div>

  </div>

</div>

</div>

</div>

<div id="sdk-for-ios-explore-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

