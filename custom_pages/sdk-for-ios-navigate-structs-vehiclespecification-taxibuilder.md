---
title: "TaxiBuilder Class Reference"
slug: "sdk-for-ios-navigate-structs-vehiclespecification-taxibuilder"
---

# TaxiBuilder

<div class="declaration">

<div class="language">

``` highlight
public class TaxiBuilder
```

``` highlight
extension VehicleSpecification.TaxiBuilder: NativeBase
```

``` highlight
extension VehicleSpecification.TaxiBuilder: Hashable
```

</div>

</div>

This class constructs a <a href="sdk-for-ios-navigate-structs-vehiclespecification">`VehicleSpecification`</a> for a taxi.

</div>

<div class="section section task-group-section">

<div class="task-group">

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

  Creates a new instance of this class.

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

      withHeightInCentimeters(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the vehicle height in centimeters.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func withHeightInCentimeters ( _ heightInCentimeters : Int32 ) -> VehicleSpecification . TaxiBuilder
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
  <td><code> </code><em><code>heightInCentimeters</code></em><code> </code></td>
  <td><div>
  <p>The vehicle height in centimeters.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The `VehicleSpecification.TaxiBuilder` object with the vehicle height set to the new value.

  </div>

  </div>

  </div>

- <div>

      withWidthInCentimeters(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the vehicle width in centimeters.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func withWidthInCentimeters ( _ widthInCentimeters : Int32 ) -> VehicleSpecification . TaxiBuilder
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
  <td><code> </code><em><code>widthInCentimeters</code></em><code> </code></td>
  <td><div>
  <p>The vehicle width in centimeters.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The `VehicleSpecification.TaxiBuilder` object with the vehicle width set to the new value.

  </div>

  </div>

  </div>

- <div>

      withLengthInCentimeters(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the vehicle length in centimeters.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func withLengthInCentimeters ( _ lengthInCentimeters : Int32 ) -> VehicleSpecification . TaxiBuilder
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
  <td><code> </code><em><code>lengthInCentimeters</code></em><code> </code></td>
  <td><div>
  <p>The vehicle length in centimeters.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The `VehicleSpecification.TaxiBuilder` object with the vehicle length set to the new value.

  </div>

  </div>

  </div>

- <div>

      withAxleCount(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the vehicle axle count.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func withAxleCount ( _ axleCount : Int32 ) -> VehicleSpecification . TaxiBuilder
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
  <td><code> </code><em><code>axleCount</code></em><code> </code></td>
  <td><div>
  <p>The vehicle axle count.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The `VehicleSpecification.TaxiBuilder` object with the axle count set to the new value.

  </div>

  </div>

  </div>

- <div>

      withKingpinToRearAxleDistanceInCentimeters(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the vehicle kingpin to rear axle distance.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func withKingpinToRearAxleDistanceInCentimeters ( _ length : Int32 ) -> VehicleSpecification . TaxiBuilder
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
  <td><code> </code><em><code>length</code></em><code> </code></td>
  <td><div>
  <p>The distance from kingpin to the rear axle.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The `VehicleSpecification.TaxiBuilder` object with the kingpin to rear axle set to the new value.

  </div>

  </div>

  </div>

- <div>

      withTrailerCount(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the vehicle trailer count.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func withTrailerCount ( _ trailerCount : Int32 ) -> VehicleSpecification . TaxiBuilder
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
  <td><code> </code><em><code>trailerCount</code></em><code> </code></td>
  <td><div>
  <p>The vehicle trailer count.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The `VehicleSpecification.TaxiBuilder` object with the trailer count set to the new value.

  </div>

  </div>

  </div>

- <div>

      withPayloadCapacityInKilograms(payloadCapacityInKilograms: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the vehicle payload capacity in kilograms.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func withPayloadCapacityInKilograms ( payloadCapacityInKilograms : Int32 ) -> VehicleSpecification . TaxiBuilder
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
  <td><code> </code><em><code>payloadCapacityInKilograms</code></em><code> </code></td>
  <td><div>
  <p>The vehicle payload capacity in kilograms.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The `VehicleSpecification.TaxiBuilder` object with the payload capacity set to the new value.

  </div>

  </div>

  </div>

- <div>

      withTrailerAxleCount(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the vehicle trailer axle count.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func withTrailerAxleCount ( _ trailerAxleCount : Int32 ) -> VehicleSpecification . TaxiBuilder
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
  <td><code> </code><em><code>trailerAxleCount</code></em><code> </code></td>
  <td><div>
  <p>The vehicle trailer axle count.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The `VehicleSpecification.TaxiBuilder` object with the trailer axle count set to the new value.

  </div>

  </div>

  </div>

- <div>

      withGrossWeightInKilograms(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the vehicle gross weight in kilograms.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func withGrossWeightInKilograms ( _ grossWeightInKilograms : Int32 ) -> VehicleSpecification . TaxiBuilder
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
  <td><code> </code><em><code>grossWeightInKilograms</code></em><code> </code></td>
  <td><div>
  <p>The vehicle gross weight in kilograms.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The `VehicleSpecification.TaxiBuilder` object with the gross weight set to the new value.

  </div>

  </div>

  </div>

- <div>

      withCurrentWeightInKilograms(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the vehicle current weight in kilograms.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func withCurrentWeightInKilograms ( _ currentWeightInKilograms : Int32 ) -> VehicleSpecification . TaxiBuilder
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
  <td><code> </code><em><code>currentWeightInKilograms</code></em><code> </code></td>
  <td><div>
  <p>The vehicle current weight in kilograms.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The `VehicleSpecification.TaxiBuilder` object with the current weight set to the new value.

  </div>

  </div>

  </div>

- <div>

      withEmptyWeightInKilograms(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the vehicle empty weight in kilograms.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func withEmptyWeightInKilograms ( _ emptyWeightInKilograms : Int32 ) -> VehicleSpecification . TaxiBuilder
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
  <td><code> </code><em><code>emptyWeightInKilograms</code></em><code> </code></td>
  <td><div>
  <p>The vehicle empty weight in kilograms.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The `VehicleSpecification.TaxiBuilder` object with the empty weight set to the new value.

  </div>

  </div>

  </div>

- <div>

      withWeightPerAxleInKilograms(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the vehicle weight per axle in kilograms.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func withWeightPerAxleInKilograms ( _ weightPerAxleInKilograms : Int32 ) -> VehicleSpecification . TaxiBuilder
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
  <td><code> </code><em><code>weightPerAxleInKilograms</code></em><code> </code></td>
  <td><div>
  <p>The vehicle weight per axle in kilograms.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The `VehicleSpecification.TaxiBuilder` object with the current weight per axle set to the new value.

  </div>

  </div>

  </div>

- <div>

      withIsCommercial(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the vehicle is commercial flag.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func withIsCommercial ( _ isCommercial : Bool ) -> VehicleSpecification . TaxiBuilder
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
  <td><code> </code><em><code>isCommercial</code></em><code> </code></td>
  <td><div>
  <p>The vehicle is commercial flag.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The `VehicleSpecification.TaxiBuilder` object with the is commercial flag set to the new value.

  </div>

  </div>

  </div>

- <div>

      withLastCharacterOfLicensePlate(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the vehicle last character of the license plate.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func withLastCharacterOfLicensePlate ( _ lastCharacterOfLicensePlate : String ) -> VehicleSpecification . TaxiBuilder
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
  <td><code> </code><em><code>lastCharacterOfLicensePlate</code></em><code> </code></td>
  <td><div>
  <p>The vehicle last character of the license plate.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The `VehicleSpecification.TaxiBuilder` object with the last character of the licence plate set to the new value.

  </div>

  </div>

  </div>

- <div>

      withEngineSizeInCubicCentimeters(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the vehicle engine size in cubic centimeters.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func withEngineSizeInCubicCentimeters ( _ engineSizeInCubicCentimeters : Int32 ) -> VehicleSpecification . TaxiBuilder
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
  <td><code> </code><em><code>engineSizeInCubicCentimeters</code></em><code> </code></td>
  <td><div>
  <p>The vehicle engine size in cubic centimeters.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The `VehicleSpecification.TaxiBuilder` object with the engine size set to the new value.

  </div>

  </div>

  </div>

- <div>

      withTiresCount(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the vehicle tires count.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func withTiresCount ( _ tiresCount : Int32 ) -> VehicleSpecification . TaxiBuilder
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
  <td><code> </code><em><code>tiresCount</code></em><code> </code></td>
  <td><div>
  <p>The vehicle tires count.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The `VehicleSpecification.TaxiBuilder` object with the vehicle tires count set to the new value.

  </div>

  </div>

  </div>

- <div>

      withTunnelCategory(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the vehicle tunnel category.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func withTunnelCategory ( _ tunnelCategory : TunnelCategory ) -> VehicleSpecification . TaxiBuilder
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
  <td><code> </code><em><code>tunnelCategory</code></em><code> </code></td>
  <td><div>
  <p>The vehicle tunnel category.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The `VehicleSpecification.TaxiBuilder` object with the vehicle tunnel category set to the new value.

  </div>

  </div>

  </div>

- <div>

      withOccupancy(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the vehicle occupants number.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func withOccupancy ( _ occupancy : Int32 ) -> VehicleSpecification . TaxiBuilder
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
  <td><code> </code><em><code>occupancy</code></em><code> </code></td>
  <td><div>
  <p>The vehicle occupants number.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The `VehicleSpecification.TaxiBuilder` object with the vehicle occupants number set to the new value.

  </div>

  </div>

  </div>

- <div>

      build()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Builds the <a href="sdk-for-ios-navigate-structs-vehiclespecification">`VehicleSpecification`</a> object for <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO4taxiyA2CmF">`TransportMode.taxi`</a> with the specifications taken from the `VehicleSpecification.TaxiBuilder` object.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func build () -> VehicleSpecification
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Return Value

  The <a href="sdk-for-ios-navigate-structs-vehiclespecification">`VehicleSpecification`</a> object created from the `VehicleSpecification.TaxiBuilder` object.

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

