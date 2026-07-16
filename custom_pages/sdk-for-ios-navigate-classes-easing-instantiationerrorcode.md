---
title: "InstantiationErrorCode Enumeration Reference"
slug: "sdk-for-ios-navigate-classes-easing-instantiationerrorcode"
---

# InstantiationErrorCode

<div class="declaration">

<div class="language">

``` highlight
public enum InstantiationErrorCode : UInt32, CaseIterable, Codable
```

``` highlight
extension Easing.InstantiationErrorCode : Error
```

</div>

Related types:

- <a href="sdk-for-ios-navigate-classes-easing">Easing</a>

</div>

Describes a reason for failing to create an <a href="sdk-for-ios-navigate-classes-easing">`Easing`</a>.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk6EasingC22InstantiationErrorCodeO29sampledDataPointCountTooSmallyA2EmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-sampledDataPointCountTooSmall" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-easing-instantiationerrorcode#sdk-for-ios-navigate-s-7heresdk6EasingC22InstantiationErrorCodeO29sampledDataPointCountTooSmallyA2EmF" class="token"><code>sampledDataPointCountTooSmall</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Number of sampled data points in the list that defines an easing function is too small (i.e. less than 2).

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case sampledDataPointCountTooSmall = 1
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk6EasingC22InstantiationErrorCodeO35sampledDataPointsFirstXValueInvalidyA2EmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-sampledDataPointsFirstXValueInvalid" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-easing-instantiationerrorcode#sdk-for-ios-navigate-s-7heresdk6EasingC22InstantiationErrorCodeO35sampledDataPointsFirstXValueInvalidyA2EmF" class="token"><code>sampledDataPointsFirstXValueInvalid</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Invalid first value of X in the list of sampled data points that define an easing function. First value of X must be 0.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case sampledDataPointsFirstXValueInvalid
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk6EasingC22InstantiationErrorCodeO34sampledDataPointsLastXValueInvalidyA2EmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-sampledDataPointsLastXValueInvalid" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-easing-instantiationerrorcode#sdk-for-ios-navigate-s-7heresdk6EasingC22InstantiationErrorCodeO34sampledDataPointsLastXValueInvalidyA2EmF" class="token"><code>sampledDataPointsLastXValueInvalid</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Invalid last value of X in the list of sampled data points that define an easing function. Last value of X must be 1.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case sampledDataPointsLastXValueInvalid
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk6EasingC22InstantiationErrorCodeO27sampledDataXValueOutOfRangeyA2EmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-sampledDataXValueOutOfRange" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-easing-instantiationerrorcode#sdk-for-ios-navigate-s-7heresdk6EasingC22InstantiationErrorCodeO27sampledDataXValueOutOfRangeyA2EmF" class="token"><code>sampledDataXValueOutOfRange</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sampled data point X values that define an easing function are out of range \[0, 1\].

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case sampledDataXValueOutOfRange
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk6EasingC22InstantiationErrorCodeO30sampledDataXValuesNonMonotonicyA2EmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-sampledDataXValuesNonMonotonic" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-easing-instantiationerrorcode#sdk-for-ios-navigate-s-7heresdk6EasingC22InstantiationErrorCodeO30sampledDataXValuesNonMonotonicyA2EmF" class="token"><code>sampledDataXValuesNonMonotonic</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sampled data point X values in the list that defines an easing function don’t increase monotonically.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case sampledDataXValuesNonMonotonic
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

