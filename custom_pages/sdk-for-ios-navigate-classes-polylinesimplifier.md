---
title: "PolylineSimplifier Class Reference"
slug: "sdk-for-ios-navigate-classes-polylinesimplifier"
---

# PolylineSimplifier

<div class="declaration">

<div class="language">

``` highlight
public class PolylineSimplifier
```

``` highlight
extension PolylineSimplifier: NativeBase
```

``` highlight
extension PolylineSimplifier: Hashable
```

</div>

</div>

PolylineSimplifier helps to reduce the number of points in the polyline by removing redundant elements using Douglas–Peucker algorithm, so that result stays within <a href="sdk-for-ios-navigate-classes-polylinesimplifier-options">`PolylineSimplifier.Options`</a>.

Typical use case is to perform input preparation step before invoking computationally heavy API. Such API have an upper limit on the input collection size and is subject to reduced performance when collection is huge. Examples of such API are:

- <a href="sdk-for-ios-navigate-classes-trafficengine">`TrafficEngine`</a> methods which accept a <a href="sdk-for-ios-navigate-structs-geocorridor">`GeoCorridor`</a>;
- `RoutePrefetcher.prefetchGeoCorridor`.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18PolylineSimplifierCACyKcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-polylinesimplifier#sdk-for-ios-navigate-s-7heresdk18PolylineSimplifierCACyKcfc" class="token"><code>init()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance of `PolylineSimplifier`.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-core#sdk-for-ios-navigate-s-7heresdk18InstantiationErrora">`InstantiationError`</a> Indicates what went wrong when the instantiation was attempted.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init() throws
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18PolylineSimplifierC7OptionsV"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Struct-Options" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-polylinesimplifier#sdk-for-ios-navigate-s-7heresdk18PolylineSimplifierC7OptionsV" class="token"><code>Options</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Controls the strategy of <a href="sdk-for-ios-navigate-classes-polylinesimplifier#sdk-for-ios-navigate-s-7heresdk18PolylineSimplifierC8simplify8polyline24simplificationParameters10completionAA10TaskHandle_pSayAA14GeoCoordinatesVG_AC7OptionsVyAA0B19SimplificationErrorOSg_AKSgtctF">`PolylineSimplifier.simplify(...)`</a> when reducing a size of polyline.

  <a href="sdk-for-ios-navigate-classes-polylinesimplifier-options" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct Options
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18PolylineSimplifierC8simplify8polyline24simplificationParameters10completionAA10TaskHandle_pSayAA14GeoCoordinatesVG_AC7OptionsVyAA0B19SimplificationErrorOSg_AKSgtctF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-simplify-polyline-simplificationParameters-completion" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-polylinesimplifier#sdk-for-ios-navigate-s-7heresdk18PolylineSimplifierC8simplify8polyline24simplificationParameters10completionAA10TaskHandle_pSayAA14GeoCoordinatesVG_AC7OptionsVyAA0B19SimplificationErrorOSg_AKSgtctF" class="token"><code>simplify(polyline:</code><wbr></wbr><code>simplificationParameters:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Reduces the number of points in the input polyline. Does this by removing points which are not significant according to the passed <a href="sdk-for-ios-navigate-classes-polylinesimplifier-options">`PolylineSimplifier.Options`</a>. Simplification process is performed on the device without connecting to the network and is computationally intensive.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func simplify(polyline: [GeoCoordinates], simplificationParameters: PolylineSimplifier.Options, completion: @escaping PolylineSimplificationCompletionHandler) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-geocoordinates">GeoCoordinates</a>
  - <a href="sdk-for-ios-navigate-classes-polylinesimplifier-options">Options</a>
  - <a href="sdk-for-ios-navigate-core#sdk-for-ios-navigate-s-7heresdk39PolylineSimplificationCompletionHandlera">PolylineSimplificationCompletionHandler</a>
  - <a href="sdk-for-ios-navigate-protocols-taskhandle">TaskHandle</a>

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
  <td><code> </code><em><code>polyline</code></em><code> </code></td>
  <td><div>
  <p>Input polyline that should be reduced in size.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>simplificationParameters</code></em><code> </code></td>
  <td><div>
  <p>Strategy, that controls the behavior of the underlying algorithm.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Callback, which will be invoked on the main thread, when operation is finished.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Controls an asynchronous operation.

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

