---
title: "MapViewLifecycleDelegate Protocol Reference"
slug: "sdk-for-ios-explore-protocols-mapviewlifecycledelegate"
---

# MapViewLifecycleDelegate

<div class="declaration">

<div class="language">

``` highlight
public protocol MapViewLifecycleDelegate : AnyObject
```

</div>

</div>

Provides a mechanism for observing a lifecycle of a map view and/or implementing components whose lifecycle needs to be linked with that of a map view.

Storing the map view in a strong reference is strongly discouraged, as that will create a reference cycle and prevent map view from being released.

A <a href="sdk-for-ios-explore-classes-mapview">`MapView`</a> is using a <a href="https://developer.apple.com/documentation/quartzcore/cametallayer">CAMetalLayer</a>

to render its content.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk24MapViewLifecycleDelegateP8onAttach2toyAA0bC4Base_p_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-onAttach-to" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-mapviewlifecycledelegate#sdk-for-ios-explore-s-7heresdk24MapViewLifecycleDelegateP8onAttach2toyAA0bC4Base_p_tF" class="token"><code>onAttach(to:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Called when adding `MapViewLifecycleDelegate` to the map view. If the map view does not have render target attached at the time of adding the listener, then this method will be called later, after render target is attached. This means that the map view it receives is always fully initialized.

  Can be used to implement the logic to create and add visual components to the map view.

  Storing the map view in a strong reference is strongly discouraged, as that will create a reference cycle and prevent map view from being released.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func onAttach(to mapView: MapViewBase)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-mapviewbase">MapViewBase</a>

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
  <td><code> </code><em><code>mapView</code></em><code> </code></td>
  <td><div>
  <p>The map view to attach to.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk24MapViewLifecycleDelegateP8onDetach4fromyAA0bC4Base_p_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-onDetach-from" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-mapviewlifecycledelegate#sdk-for-ios-explore-s-7heresdk24MapViewLifecycleDelegateP8onDetach4fromyAA0bC4Base_p_tF" class="token"><code>onDetach(from:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Called when removing `MapViewLifecycleDelegate` from the map view. Can be used to implement the logic to remove visual components from the map view and release resources if necessary.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func onDetach(from mapView: MapViewBase)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-mapviewbase">MapViewBase</a>

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
  <td><code> </code><em><code>mapView</code></em><code> </code></td>
  <td><div>
  <p>The map view to detach from.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk24MapViewLifecycleDelegateP7onPauseyyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-onPause" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-mapviewlifecycledelegate#sdk-for-ios-explore-s-7heresdk24MapViewLifecycleDelegateP7onPauseyyF" class="token"><code>onPause()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Called when the map view to which this `MapViewLifecycleDelegate` is attached to gets paused (usually when the app goes into background). This should be used by components that perform continuous updates to pause those updates until <a href="sdk-for-ios-explore-protocols-mapviewlifecycledelegate#sdk-for-ios-explore-s-7heresdk24MapViewLifecycleDelegateP8onResumeyyF">`onResume(...)`</a> is called.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func onPause()
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk24MapViewLifecycleDelegateP8onResumeyyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-onResume" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-mapviewlifecycledelegate#sdk-for-ios-explore-s-7heresdk24MapViewLifecycleDelegateP8onResumeyyF" class="token"><code>onResume()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Called when the map view to which this `MapViewLifecycleDelegate` is attached to gets resumed (usually when the app goes into foreground). This should be used by components that perform continuous updates to resume those updates after a previous call to <a href="sdk-for-ios-explore-protocols-mapviewlifecycledelegate#sdk-for-ios-explore-s-7heresdk24MapViewLifecycleDelegateP7onPauseyyF">`onPause(...)`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func onResume()
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk24MapViewLifecycleDelegateP9onDestroyyyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-onDestroy" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-mapviewlifecycledelegate#sdk-for-ios-explore-s-7heresdk24MapViewLifecycleDelegateP9onDestroyyyF" class="token"><code>onDestroy()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Called when the map view to which this is attached to is destroyed. After this is called, no other `MapViewLifecycleDelegate` method will be invoked. This should be used to make sure all resources are freed.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func onDestroy()
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

