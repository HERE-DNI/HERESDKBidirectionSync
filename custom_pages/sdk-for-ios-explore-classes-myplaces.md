---
title: "MyPlaces Class Reference"
slug: "sdk-for-ios-explore-classes-myplaces"
---

# MyPlaces

<div class="declaration">

<div class="language">

``` highlight
public class MyPlaces
```

``` highlight
extension MyPlaces: NativeBase
```

``` highlight
extension MyPlaces: Hashable
```

</div>

</div>

Provides means to populate personal places data source. Also acts as a owner of the collection of personal places. MyPlaces is memory-only object: nothing is persisted and/or sent over the network. Client has full control on how to store personal places.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8MyPlacesCACycfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-myplaces#sdk-for-ios-explore-s-7heresdk8MyPlacesCACycfc" class="token"><code>init()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance of this class.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init()
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8MyPlacesC6placesSayAA8GeoPlaceVGvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-places" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-myplaces#sdk-for-ios-explore-s-7heresdk8MyPlacesC6placesSayAA8GeoPlaceVGvp" class="token"><code>places</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of places which currently belong to this data source. This list is a clone of the internal list and thus changing it has no effect on the data source.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var places: [GeoPlace] { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geoplace">GeoPlace</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8MyPlacesC8addPlace5place8callbackAA10TaskHandle_pAA03GeoE0V_yAA0H7OutcomeOctF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-addPlace-place-callback" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-myplaces#sdk-for-ios-explore-s-7heresdk8MyPlacesC8addPlace5place8callbackAA10TaskHandle_pAA03GeoE0V_yAA0H7OutcomeOctF" class="token"><code>addPlace(place:</code><wbr></wbr><code>callback:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds a place to this data source.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func addPlace(place: GeoPlace, callback: @escaping TaskCompletionHandler) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geoplace">GeoPlace</a>
  - <a href="sdk-for-ios-explore-core#sdk-for-ios-explore-s-7heresdk21TaskCompletionHandlera">TaskCompletionHandler</a>
  - <a href="sdk-for-ios-explore-protocols-taskhandle">TaskHandle</a>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>place</code></em><code> </code></td>
  <td><div>
  <p>The place.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>callback</code></em><code> </code></td>
  <td><div>
  <p>The callback to be called when task is completed.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate the execution of the task.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8MyPlacesC03addC06places8callbackAA10TaskHandle_pSayAA8GeoPlaceVG_yAA0G7OutcomeOctF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-addPlaces-places-callback" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-myplaces#sdk-for-ios-explore-s-7heresdk8MyPlacesC03addC06places8callbackAA10TaskHandle_pSayAA8GeoPlaceVG_yAA0G7OutcomeOctF" class="token"><code>addPlaces(places:</code><wbr></wbr><code>callback:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds a list of places to this data source.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func addPlaces(places: [GeoPlace], callback: @escaping TaskCompletionHandler) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geoplace">GeoPlace</a>
  - <a href="sdk-for-ios-explore-core#sdk-for-ios-explore-s-7heresdk21TaskCompletionHandlera">TaskCompletionHandler</a>
  - <a href="sdk-for-ios-explore-protocols-taskhandle">TaskHandle</a>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>places</code></em><code> </code></td>
  <td><div>
  <p>Places</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>callback</code></em><code> </code></td>
  <td><div>
  <p>The callback to be called when task is completed.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate the execution of the task.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8MyPlacesC11removePlace7placeId8callbackAA10TaskHandle_pSS_yAA0I7OutcomeOctF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-removePlace-placeId-callback" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-myplaces#sdk-for-ios-explore-s-7heresdk8MyPlacesC11removePlace7placeId8callbackAA10TaskHandle_pSS_yAA0I7OutcomeOctF" class="token"><code>removePlace(placeId:</code><wbr></wbr><code>callback:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes a place from this data source.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func removePlace(placeId: String, callback: @escaping TaskCompletionHandler) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-core#sdk-for-ios-explore-s-7heresdk21TaskCompletionHandlera">TaskCompletionHandler</a>
  - <a href="sdk-for-ios-explore-protocols-taskhandle">TaskHandle</a>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>placeId</code></em><code> </code></td>
  <td><div>
  <p>The place id</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>callback</code></em><code> </code></td>
  <td><div>
  <p>The callback to be called when task is completed.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate the execution of the task.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8MyPlacesC06removeC08placeIds8callbackAA10TaskHandle_pSaySSG_yAA0H7OutcomeOctF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-removePlaces-placeIds-callback" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-myplaces#sdk-for-ios-explore-s-7heresdk8MyPlacesC06removeC08placeIds8callbackAA10TaskHandle_pSaySSG_yAA0H7OutcomeOctF" class="token"><code>removePlaces(placeIds:</code><wbr></wbr><code>callback:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes a list of places from this data source.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func removePlaces(placeIds: [String], callback: @escaping TaskCompletionHandler) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-core#sdk-for-ios-explore-s-7heresdk21TaskCompletionHandlera">TaskCompletionHandler</a>
  - <a href="sdk-for-ios-explore-protocols-taskhandle">TaskHandle</a>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>placeIds</code></em><code> </code></td>
  <td><div>
  <p>Place ids</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>callback</code></em><code> </code></td>
  <td><div>
  <p>The callback to be called when task is completed.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate the execution of the task.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8MyPlacesC9removeAll8callbackAA10TaskHandle_pyAA0G7OutcomeOc_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-removeAll-callback" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-myplaces#sdk-for-ios-explore-s-7heresdk8MyPlacesC9removeAll8callbackAA10TaskHandle_pyAA0G7OutcomeOc_tF" class="token"><code>removeAll(callback:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes all places from this data source.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func removeAll(callback: @escaping TaskCompletionHandler) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-core#sdk-for-ios-explore-s-7heresdk21TaskCompletionHandlera">TaskCompletionHandler</a>
  - <a href="sdk-for-ios-explore-protocols-taskhandle">TaskHandle</a>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>callback</code></em><code> </code></td>
  <td><div>
  <p>The callback to be called when task is completed.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate the execution of the task.

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

