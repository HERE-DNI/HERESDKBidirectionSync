---
title: "Easing Class Reference"
slug: "sdk-for-ios-navigate-classes-easing"
---

# Easing

<div class="declaration">

<div class="language">

``` highlight
public class Easing
```

``` highlight
extension Easing: NativeBase
```

``` highlight
extension Easing: Hashable
```

</div>

</div>

Animation easing representing an easing function to be used during animations.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk6EasingC18InstantiationErrora"></span>` `<span id="//apple_ref/swift/Alias/InstantiationError" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-easing#/s:7heresdk6EasingC18InstantiationErrora" class="token"><code>InstantiationError</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Thrown when a problem occurs while trying to create an `Easing`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias InstantiationError = InstantiationErrorCode
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates an instance of `Easing` using a predefined easing function.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( _ easingFunction : EasingFunction )
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
  <td><code> </code><em><code>easingFunction</code></em><code> </code></td>
  <td><div>
  <p>Easing function.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      init(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates an instance of customized `Easing` using a specified number of points describing an easing function.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-classes-easing#/s:7heresdk6EasingC18InstantiationErrora">`Easing.InstantiationError`</a> Instantiation error in case of invalid input parameters.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( _ points : [ Point2D ]) throws
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
  <td><code> </code><em><code>points</code></em><code> </code></td>
  <td><div>
  <p>List of sampled data points that define an easing function. X describes normalized time values in the range [0, 1]. Y describes normalized animated value changes. Values can fall outside of the range [0, 1]. During an animation run animated target value is multiplied with Y value. In case resulting animated target value falls outside of its own supported range it will be clamped to its range (e.g. when negative values used for color animation). X values must increase monotonically. There must be at least 2 data points specified. The first point’s X value must be 0, the last point’s X value must be 1. During an animation run for any given time value X’ from the animation engine that satisfies the relation X(i) &lt; X’ &lt; X(i+1) for the given X data points the corresponding Y’ value will be calculated by linearly interpolating between Y(i) and Y(i+1) data points. The higher the sampling rate of the easing curve used for the data points the more precise the results. In order to achieve the same animation precision for animations with different durations (shorter vs longer) it is recommended to use a higher sampling rate for longer animation duration.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk6EasingC22InstantiationErrorCodeO"></span>` `<span id="//apple_ref/swift/Enum/InstantiationErrorCode" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-easing#/s:7heresdk6EasingC22InstantiationErrorCodeO" class="token"><code>InstantiationErrorCode</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Describes a reason for failing to create an <a href="sdk-for-ios-navigate-classes-easing">`Easing`</a>.

  <a href="sdk-for-ios-navigate-classes-easing-instantiationerrorcode" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum InstantiationErrorCode : UInt32, CaseIterable, Codable
  ```

  ``` highlight
  extension Easing.InstantiationErrorCode : Error
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

