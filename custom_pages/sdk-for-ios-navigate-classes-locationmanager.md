---
title: "LocationManager Class Reference"
slug: "sdk-for-ios-navigate-classes-locationmanager"
---

# LocationManager

<div class="declaration">

<div class="language">

``` highlight
public class LocationManager : LocationDelegate
```

``` highlight
extension LocationManager: NativeBase
```

``` highlight
extension LocationManager: Hashable
```

</div>

</div>

LocationManager listens to position updates and provides the map-matched location using the LocationManagerListener.

**Note:** This is a **beta** release of this feature. There may be bugs and unexpected behaviors. Related APIs may change in future releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

      init(sdkEngine: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance of `LocationManager`.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-core#/s:7heresdk18InstantiationErrora">`InstantiationError`</a> Instantiation error.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( sdkEngine : SDKNativeEngine ) throws
  ```

  </pre>

  </div>

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
  <td><code> </code><em><code>sdkEngine</code></em><code> </code></td>
  <td><div>
  <p>A SDKEngine instance.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      onLocationUpdated(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Called each time a new location is available. In a navigation context while using the <a href="sdk-for-ios-navigate-classes-navigator">`Navigator`</a> or <a href="sdk-for-ios-navigate-classes-visualnavigator">`VisualNavigator`</a>, it’s required to set the <a href="sdk-for-ios-navigate-structs-location#/s:7heresdk8LocationV4time10Foundation4DateVSgvp">`Location.time`</a> parameter for each <a href="sdk-for-ios-navigate-structs-location">`Location`</a> object so that the HERE SDK can map-match the locations properly. If the <a href="sdk-for-ios-navigate-structs-location#/s:7heresdk8LocationV4time10Foundation4DateVSgvp">`Location.time`</a> parameter is missing, the location will be ignored. For navigation, it is also recommended to provide the `bearing` and `speed` parameters for each <a href="sdk-for-ios-navigate-structs-location">`Location`</a> object. Invoked on the main thread.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func onLocationUpdated ( _ location : Location )
  ```

  </pre>

  </div>

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
  <td><code> </code><em><code>location</code></em><code> </code></td>
  <td><div>
  <p>Current location.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      setMapMatcher(mapMatcher: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the <a href="sdk-for-ios-navigate-classes-mapmatcher">`MapMatcher`</a> for exclusive use by `LocationManager`.

  **Threading:** This method is asynchronous and performs the switch in an internal thread of `LocationManager`. **Note:** After calling this method, the <a href="sdk-for-ios-navigate-classes-mapmatcher">`MapMatcher`</a> is owned and used exclusively by `LocationManager` in its internal processing thread. Do not use or access the <a href="sdk-for-ios-navigate-classes-mapmatcher">`MapMatcher`</a> elsewhere while it is set.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setMapMatcher ( mapMatcher : MapMatcher ?)
  ```

  </pre>

  </div>

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
  <td><code> </code><em><code>mapMatcher</code></em><code> </code></td>
  <td><div>
  <p>The <a href="sdk-for-ios-navigate-classes-mapmatcher"><code>MapMatcher</code></a> instance to be used exclusively by <code>LocationManager</code>.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      takeMapMatcher()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Retrieves and removes the <a href="sdk-for-ios-navigate-classes-mapmatcher">`MapMatcher`</a> from `LocationManager`. **Note:** After calling this method, `LocationManager` will no longer use the <a href="sdk-for-ios-navigate-classes-mapmatcher">`MapMatcher`</a> at all. the caller regains full ownership and responsibility for the <a href="sdk-for-ios-navigate-classes-mapmatcher">`MapMatcher`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func takeMapMatcher () -> MapMatcher ?
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Return Value

  The <a href="sdk-for-ios-navigate-classes-mapmatcher">`MapMatcher`</a> instance previously set, or `nil` if none was set.

  </div>

  </div>

  </div>

- <div>

      MatchedLocationDelegate(matchedLocationListener: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds the <a href="sdk-for-ios-navigate-protocols-matchedlocationlistener">`MatchedLocationListener`</a> to the subscribtion list.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func MatchedLocationDelegate ( matchedLocationListener : MatchedLocationListener )
  ```

  </pre>

  </div>

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
  <td><code> </code><em><code>matchedLocationListener</code></em><code> </code></td>
  <td><div>
  <p>Listener to be added to the map matched location updates.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      removeMatchedLocationListener(matchedLocationListener: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes the <a href="sdk-for-ios-navigate-protocols-matchedlocationlistener">`MatchedLocationListener`</a> from the subscribtion list.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func removeMatchedLocationListener ( matchedLocationListener : MatchedLocationListener )
  ```

  </pre>

  </div>

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
  <td><code> </code><em><code>matchedLocationListener</code></em><code> </code></td>
  <td><div>
  <p>Listener to be removed from the map matched location updates.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

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

