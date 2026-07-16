---
title: "Calculation Structure Reference"
slug: "sdk-for-ios-navigate-structs-isolineoptions-calculation"
---

# Calculation

<div class="declaration">

<div class="language">

``` highlight
public struct Calculation
```

</div>

</div>

Specifies isoline parameters. Setting at least one limit to <a href="sdk-for-ios-navigate-structs-isolineoptions-calculation#sdk-for-ios-navigate-s-7heresdk14IsolineOptionsV11CalculationV11rangeValuesSays5Int32VGvp">`IsolineOptions.Calculation.rangeValues`</a> is mandatory or the calculation will fail.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14IsolineOptionsV11CalculationV9rangeTypeAA0b5RangeF0Ovp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-rangeType" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-isolineoptions-calculation#sdk-for-ios-navigate-s-7heresdk14IsolineOptionsV11CalculationV9rangeTypeAA0b5RangeF0Ovp" class="token"><code>rangeType</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies the range of values to be included in the isoline.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var rangeType: IsolineRangeType
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-isolinerangetype">IsolineRangeType</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14IsolineOptionsV11CalculationV11rangeValuesSays5Int32VGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-rangeValues" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-isolineoptions-calculation#sdk-for-ios-navigate-s-7heresdk14IsolineOptionsV11CalculationV11rangeValuesSays5Int32VGvp" class="token"><code>rangeValues</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A list of ranges. The unit is defined by the type parameter. Each range defines the maximum allowed value to reach a destination. For each value an <a href="sdk-for-ios-navigate-classes-isoline">`Isoline`</a> is calculated indicating the reachable area. If empty, <a href="sdk-for-ios-navigate-structs-isolineoptions">`IsolineOptions`</a> object is considered invalid.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var rangeValues: [Int32]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14IsolineOptionsV11CalculationV07isolineD4ModeAA0bdF0Ovp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-isolineCalculationMode" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-isolineoptions-calculation#sdk-for-ios-navigate-s-7heresdk14IsolineOptionsV11CalculationV07isolineD4ModeAA0bdF0Ovp" class="token"><code>isolineCalculationMode</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies how isoline calculation is optimized. The default waypoint type is <a href="sdk-for-ios-navigate-enums-isolinecalculationmode#sdk-for-ios-navigate-s-7heresdk22IsolineCalculationModeO8balancedyA2CmF">`IsolineCalculationMode.balanced`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isolineCalculationMode: IsolineCalculationMode
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-isolinecalculationmode">IsolineCalculationMode</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14IsolineOptionsV11CalculationV9maxPointss5Int32VSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-maxPoints" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-isolineoptions-calculation#sdk-for-ios-navigate-s-7heresdk14IsolineOptionsV11CalculationV9maxPointss5Int32VSgvp" class="token"><code>maxPoints</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Limits the number of points in the resulting isoline polygon. If the isoline consists of multiple polygons, the sum of points from all polygons is considered. Note that this parameter does not affect the calculation, but the shape of the polygon. Look at <a href="sdk-for-ios-navigate-enums-isolinecalculationmode">`IsolineCalculationMode`</a> parameter to optimize performance. A higher value will result in a more accurate polygon shape. Rendering a polygon with a high number of points can negatively impact rendering performance. The minimum allowed value is 30, lower values will be ignored.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var maxPoints: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14IsolineOptionsV11CalculationV16isolineDirectionAA010RoutePlaceF0Ovp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-isolineDirection" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-isolineoptions-calculation#sdk-for-ios-navigate-s-7heresdk14IsolineOptionsV11CalculationV16isolineDirectionAA010RoutePlaceF0Ovp" class="token"><code>isolineDirection</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies if calculations will be from or to a specific point. The default isoline direction is <a href="sdk-for-ios-navigate-enums-routeplacedirection#sdk-for-ios-navigate-s-7heresdk19RoutePlaceDirectionO9departureyA2CmF">`RoutePlaceDirection.departure`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isolineDirection: RoutePlaceDirection
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-routeplacedirection">RoutePlaceDirection</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14IsolineOptionsV11CalculationV9rangeType0E6ValuesAeA0b5RangeF0O_Says5Int32VGtcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-rangeType-rangeValues" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-isolineoptions-calculation#sdk-for-ios-navigate-s-7heresdk14IsolineOptionsV11CalculationV9rangeType0E6ValuesAeA0b5RangeF0O_Says5Int32VGtcfc" class="token"><code>init(rangeType:</code><wbr></wbr><code>rangeValues:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(rangeType: IsolineRangeType, rangeValues: [Int32])
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-isolinerangetype">IsolineRangeType</a>

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
  <td><code> </code><em><code>rangeType</code></em><code> </code></td>
  <td><div>
  <p>The range type.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>rangeValues</code></em><code> </code></td>
  <td><div>
  <p>Range values.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14IsolineOptionsV11CalculationV9rangeType0E6Values16isolineDirectionAeA0b5RangeF0O_Says5Int32VGAA010RoutePlaceI0Otcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-rangeType-rangeValues-isolineDirection" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-isolineoptions-calculation#sdk-for-ios-navigate-s-7heresdk14IsolineOptionsV11CalculationV9rangeType0E6Values16isolineDirectionAeA0b5RangeF0O_Says5Int32VGAA010RoutePlaceI0Otcfc" class="token"><code>init(rangeType:</code><wbr></wbr><code>rangeValues:</code><wbr></wbr><code>isolineDirection:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(rangeType: IsolineRangeType, rangeValues: [Int32], isolineDirection: RoutePlaceDirection)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-isolinerangetype">IsolineRangeType</a>
  - <a href="sdk-for-ios-navigate-enums-routeplacedirection">RoutePlaceDirection</a>

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
  <td><code> </code><em><code>rangeType</code></em><code> </code></td>
  <td><div>
  <p>The range type.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>rangeValues</code></em><code> </code></td>
  <td><div>
  <p>Range values.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>isolineDirection</code></em><code> </code></td>
  <td><div>
  <p>The isoline direction.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14IsolineOptionsV11CalculationV9rangeType0E6Values07isolineD4ModeAeA0b5RangeF0O_Says5Int32VGAA0bdI0Otcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-rangeType-rangeValues-isolineCalculationMode" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-isolineoptions-calculation#sdk-for-ios-navigate-s-7heresdk14IsolineOptionsV11CalculationV9rangeType0E6Values07isolineD4ModeAeA0b5RangeF0O_Says5Int32VGAA0bdI0Otcfc" class="token"><code>init(rangeType:</code><wbr></wbr><code>rangeValues:</code><wbr></wbr><code>isolineCalculationMode:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(rangeType: IsolineRangeType, rangeValues: [Int32], isolineCalculationMode: IsolineCalculationMode)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-isolinerangetype">IsolineRangeType</a>
  - <a href="sdk-for-ios-navigate-enums-isolinecalculationmode">IsolineCalculationMode</a>

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
  <td><code> </code><em><code>rangeType</code></em><code> </code></td>
  <td><div>
  <p>The range type.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>rangeValues</code></em><code> </code></td>
  <td><div>
  <p>Range values.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>isolineCalculationMode</code></em><code> </code></td>
  <td><div>
  <p>The isoline calculation mode.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14IsolineOptionsV11CalculationV9rangeType0E6Values07isolineD4Mode9maxPoints0H9DirectionAeA0b5RangeF0O_Says5Int32VGAA0bdI0OANSgAA010RoutePlaceL0Otcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-rangeType-rangeValues-isolineCalculationMode-maxPoints-isolineDirection" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-isolineoptions-calculation#sdk-for-ios-navigate-s-7heresdk14IsolineOptionsV11CalculationV9rangeType0E6Values07isolineD4Mode9maxPoints0H9DirectionAeA0b5RangeF0O_Says5Int32VGAA0bdI0OANSgAA010RoutePlaceL0Otcfc" class="token"><code>init(rangeType:</code><wbr></wbr><code>rangeValues:</code><wbr></wbr><code>isolineCalculationMode:</code><wbr></wbr><code>maxPoints:</code><wbr></wbr><code>isolineDirection:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(rangeType: IsolineRangeType, rangeValues: [Int32], isolineCalculationMode: IsolineCalculationMode, maxPoints: Int32?, isolineDirection: RoutePlaceDirection)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-isolinerangetype">IsolineRangeType</a>
  - <a href="sdk-for-ios-navigate-enums-isolinecalculationmode">IsolineCalculationMode</a>
  - <a href="sdk-for-ios-navigate-enums-routeplacedirection">RoutePlaceDirection</a>

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
  <td><code> </code><em><code>rangeType</code></em><code> </code></td>
  <td><div>
  <p>The range type.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>rangeValues</code></em><code> </code></td>
  <td><div>
  <p>Range values.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>isolineCalculationMode</code></em><code> </code></td>
  <td><div>
  <p>The isoline calculation mode.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>maxPoints</code></em><code> </code></td>
  <td><div>
  <p>The max points number.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>isolineDirection</code></em><code> </code></td>
  <td><div>
  <p>The isoline direction.</p>
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

