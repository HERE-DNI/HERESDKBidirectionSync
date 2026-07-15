---
title: "AngleRange Structure Reference"
slug: "sdk-for-ios-navigate-structs-anglerange"
---

# AngleRange

<div class="declaration">

<div class="language">

``` highlight
public struct AngleRange : Hashable
```

</div>

</div>

Represents angle ranges as a circular sector by using an absolute start angle and a relative range angle called extent. They both define a sector on a circle. All angles are in degrees and are clockwise-oriented. By default, the AngleRange represents the entire circle, the value is in the range of \[0, 360\]. Values will be corrected during construction using normalization for the start angle and clamping for the extent angle, ensuring a valid range for all possible inputs.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk10AngleRangeV5startSdvp"></span>` `<span id="//apple_ref/swift/Property/start" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-anglerange#/s:7heresdk10AngleRangeV5startSdvp" class="token"><code>start</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Start angle, running clockwise, in degrees from north. The value is in the range of \[0, 360) degrees.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public let start: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10AngleRangeV6extentSdvp"></span>` `<span id="//apple_ref/swift/Property/extent" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-anglerange#/s:7heresdk10AngleRangeV6extentSdvp" class="token"><code>extent</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The angle range extent, running clockwise, in degrees from start. The value is in the range of \[0, 360\] degrees.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public let extent: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(start: extent: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs an AngleRange from the provided start and extent angles. Corrects values if they exceed the ranges.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( start : Double , extent : Double )
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
  <td><code> </code><em><code>start</code></em><code> </code></td>
  <td><div>
  <p>Start angle, running clockwise, in degrees from north. The value will be normalized to [0.0, 360.0).</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>extent</code></em><code> </code></td>
  <td><div>
  <p>The range’s extent, running clockwise, in degrees from start. The value will be clamped to the range of [0, 360] degrees.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      init()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs a range covering a full circle.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ()
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

      fromMinMaxDegreesClockwise(min: max: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs an AngleRange from the provided minimum and maximum angles. Corrects values if they exceed the ranges. The angles are always interpreted in clockwise orientation.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func fromMinMaxDegreesClockwise ( min : Double , max : Double ) -> AngleRange
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
  <td><code> </code><em><code>min</code></em><code> </code></td>
  <td><div>
  <p>Angle where to start the circular sector, running clockwise, in degrees from north. The value will be normalized to [0.0, 360.0).</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>max</code></em><code> </code></td>
  <td><div>
  <p>Angle where the circular sector ends, running clockwise, in degrees from north. The value will be normalized to [0.0, 360.0).</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Created AngleRange from the provided minimum and maximum angles.

  </div>

  </div>

  </div>

- <div>

      fromDirectionDegreesClockwise(center: extent: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs an AngleRange from the provided center angle defining the direction and an angular width to extent the range by 50% clockwise and 50% counter-clockwise from its center angle. Corrects values if they exceed the ranges. Example: direction = 90, extent = 10 means the circle sector is pointing east, with an extent of 5 degrees north-wards and 5 degrees south-wards.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func fromDirectionDegreesClockwise ( center : Double , extent : Double ) -> AngleRange
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
  <td><code> </code><em><code>center</code></em><code> </code></td>
  <td><div>
  <p>Start angle, running clockwise, in degrees from north. The value will be normalized to [0.0, 360.0).</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>extent</code></em><code> </code></td>
  <td><div>
  <p>The range’s extent, running clockwise, in degrees from start. The value will be clamped to the range of [0, 360] degrees.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Created AngleRange from the provided center angle and the range’s extent.

  </div>

  </div>

  </div>

- <div>

      inRange(angleClockwiseInDegreesFromNorth: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Check if a given angle in degrees, clockwise from north is in range or not.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func inRange ( angleClockwiseInDegreesFromNorth : Double ) -> Bool
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
  <td><code> </code><em><code>angleClockwiseInDegreesFromNorth</code></em><code> </code></td>
  <td><div>
  <p>An angle in degrees from north. Will be normalized before testing.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  `True`, if an angle is in range, `false` otherwise.

  </div>

  </div>

  </div>

- <div>

      closestInRange(angleClockwiseInDegreesFromNorth: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Get the angle that is closest to the given one and in range. If the angle to both ends of the range is the same, the value in the clockwise direction is returned. If the given angle is in range already, it will be returned as normalized angle.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func closestInRange ( angleClockwiseInDegreesFromNorth : Double ) -> Double
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
  <td><code> </code><em><code>angleClockwiseInDegreesFromNorth</code></em><code> </code></td>
  <td><div>
  <p>An angle in degrees from north. Will be normalized.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The closest, normalized in-range angle in degrees, clockwise from north. If the given angle is in range already, the given angle will be returned as normalized angle in degree, clockwise from north.

  </div>

  </div>

  </div>

- <div>

      max()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Get the maximum angle defined by the range in degrees, clockwise from north, normalized to \[0,360).

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func max () -> Double
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Return Value

  Maximum angle of the range in degrees, clockwise from north, normalized to \[0,360).

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

