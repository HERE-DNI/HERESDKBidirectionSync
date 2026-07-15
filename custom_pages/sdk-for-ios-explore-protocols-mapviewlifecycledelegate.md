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

      onAttach(to: )

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
  func onAttach ( to mapView : MapViewBase )
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

      onDetach(from: )

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
  func onDetach ( from mapView : MapViewBase )
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

      onPause()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Called when the map view to which this `MapViewLifecycleDelegate` is attached to gets paused (usually when the app goes into background). This should be used by components that perform continuous updates to pause those updates until

      onResume(...)

  is called.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func onPause ()
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

      onResume()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Called when the map view to which this `MapViewLifecycleDelegate` is attached to gets resumed (usually when the app goes into foreground). This should be used by components that perform continuous updates to resume those updates after a previous call to

      onPause(...)

  .
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func onResume ()
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

      onDestroy()

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
  func onDestroy ()
  ```

  </pre>

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

