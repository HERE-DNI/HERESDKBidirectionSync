---
title: "Gestures Class Reference"
slug: "sdk-for-ios-navigate-classes-gestures"
---

# Gestures

<div class="declaration">

<div class="language">

``` highlight
public class Gestures
```

``` highlight
extension Gestures: NativeBase
```

``` highlight
extension Gestures: Hashable
```

</div>

</div>

Use this class to process touch events from the platform and detect gesture induced actions on the map view. Please note that this class holds strong references to the gesture delegates.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8GesturesC11tapDelegateAA03TapD0_pSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-tapDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-gestures#sdk-for-ios-navigate-s-7heresdk8GesturesC11tapDelegateAA03TapD0_pSgvp" class="token"><code>tapDelegate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  <a href="sdk-for-ios-navigate-protocols-tapdelegate">`TapDelegate`</a> that notifies when a tap gesture occurs. `Gestures` holds a strong reference to the delegate.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public weak var tapDelegate: TapDelegate? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-protocols-tapdelegate">TapDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8GesturesC17doubleTapDelegateAA06DoubledE0_pSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-doubleTapDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-gestures#sdk-for-ios-navigate-s-7heresdk8GesturesC17doubleTapDelegateAA06DoubledE0_pSgvp" class="token"><code>doubleTapDelegate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  <a href="sdk-for-ios-navigate-protocols-doubletapdelegate">`DoubleTapDelegate`</a> that notifies when a double-tap gesture occurs. `Gestures` holds a strong reference to the delegate.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public weak var doubleTapDelegate: DoubleTapDelegate? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-protocols-doubletapdelegate">DoubleTapDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8GesturesC19pinchRotateDelegateAA05PinchdE0_pSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-pinchRotateDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-gestures#sdk-for-ios-navigate-s-7heresdk8GesturesC19pinchRotateDelegateAA05PinchdE0_pSgvp" class="token"><code>pinchRotateDelegate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  <a href="sdk-for-ios-navigate-protocols-pinchrotatedelegate">`PinchRotateDelegate`</a> that notifies when a pinch-rotate gesture occurs. `Gestures` holds a strong reference to the delegate.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public weak var pinchRotateDelegate: PinchRotateDelegate? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-protocols-pinchrotatedelegate">PinchRotateDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8GesturesC17longPressDelegateAA04LongdE0_pSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-longPressDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-gestures#sdk-for-ios-navigate-s-7heresdk8GesturesC17longPressDelegateAA04LongdE0_pSgvp" class="token"><code>longPressDelegate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  <a href="sdk-for-ios-navigate-protocols-longpressdelegate">`LongPressDelegate`</a> that notifies when a long-press gesture occurs. `Gestures` holds a strong reference to the delegate.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public weak var longPressDelegate: LongPressDelegate? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-protocols-longpressdelegate">LongPressDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8GesturesC11panDelegateAA03PanD0_pSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-panDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-gestures#sdk-for-ios-navigate-s-7heresdk8GesturesC11panDelegateAA03PanD0_pSgvp" class="token"><code>panDelegate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  <a href="sdk-for-ios-navigate-protocols-pandelegate">`PanDelegate`</a> that notifies when a pan gesture occurs. `Gestures` holds a strong reference to the delegate.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public weak var panDelegate: PanDelegate? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-protocols-pandelegate">PanDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8GesturesC20twoFingerTapDelegateAA03TwodeF0_pSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-twoFingerTapDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-gestures#sdk-for-ios-navigate-s-7heresdk8GesturesC20twoFingerTapDelegateAA03TwodeF0_pSgvp" class="token"><code>twoFingerTapDelegate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  <a href="sdk-for-ios-navigate-protocols-twofingertapdelegate">`TwoFingerTapDelegate`</a> that notifies when a two-finger tap gesture occurs. `Gestures` holds a strong reference to the delegate.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public weak var twoFingerTapDelegate: TwoFingerTapDelegate? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-protocols-twofingertapdelegate">TwoFingerTapDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8GesturesC20twoFingerPanDelegateAA03TwodeF0_pSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-twoFingerPanDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-gestures#sdk-for-ios-navigate-s-7heresdk8GesturesC20twoFingerPanDelegateAA03TwodeF0_pSgvp" class="token"><code>twoFingerPanDelegate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  <a href="sdk-for-ios-navigate-protocols-twofingerpandelegate">`TwoFingerPanDelegate`</a> that notifies when a two-finger pan gesture occurs. `Gestures` holds a strong reference to the delegate.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public weak var twoFingerPanDelegate: TwoFingerPanDelegate? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-protocols-twofingerpandelegate">TwoFingerPanDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8GesturesC19enableDefaultAction10forGestureyAA0G4TypeO_tF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-enableDefaultAction-forGesture" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-gestures#sdk-for-ios-navigate-s-7heresdk8GesturesC19enableDefaultAction10forGestureyAA0G4TypeO_tF" class="token"><code>enableDefaultAction(forGesture:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Enables default action to be performed for a specified gesture.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func enableDefaultAction(forGesture gestureType: GestureType)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-gesturetype">GestureType</a>

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
  <td><code> </code><em><code>gestureType</code></em><code> </code></td>
  <td><div>
  <p>The gesture type.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8GesturesC20disableDefaultAction10forGestureyAA0G4TypeO_tF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-disableDefaultAction-forGesture" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-gestures#sdk-for-ios-navigate-s-7heresdk8GesturesC20disableDefaultAction10forGestureyAA0G4TypeO_tF" class="token"><code>disableDefaultAction(forGesture:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Disables default action for a specified gesture.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func disableDefaultAction(forGesture gestureType: GestureType)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-gesturetype">GestureType</a>

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
  <td><code> </code><em><code>gestureType</code></em><code> </code></td>
  <td><div>
  <p>The gesture type.</p>
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

