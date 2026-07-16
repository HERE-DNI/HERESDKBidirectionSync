---
title: "IsolineOptions Structure Reference"
slug: "sdk-for-ios-explore-structs-isolineoptions"
---

# IsolineOptions

<div class="declaration">

<div class="language">

``` highlight
public struct IsolineOptions
```

</div>

</div>

Specifies options for isolines calculation.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14IsolineOptionsV011calculationC0AC11CalculationVvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-calculationOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-isolineoptions#sdk-for-ios-explore-s-7heresdk14IsolineOptionsV011calculationC0AC11CalculationVvp" class="token"><code>calculationOptions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies isoline parameters.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var calculationOptions: IsolineOptions.Calculation
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-isolineoptions-calculation">Calculation</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14IsolineOptionsV03carC0AA03CarC0VSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-carOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-isolineoptions#sdk-for-ios-explore-s-7heresdk14IsolineOptionsV03carC0AA03CarC0VSgvp" class="token"><code>carOptions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies options for calculation of isolines for car. Mutually exclusive with <a href="sdk-for-ios-explore-structs-isolineoptions#sdk-for-ios-explore-s-7heresdk14IsolineOptionsV05truckC0AA05TruckC0VSgvp">`IsolineOptions.truckOptions`</a>, <a href="sdk-for-ios-explore-structs-isolineoptions#sdk-for-ios-explore-s-7heresdk14IsolineOptionsV05evCarC0AA05EVCarC0VSgvp">`IsolineOptions.evCarOptions`</a>, <a href="sdk-for-ios-explore-structs-isolineoptions#sdk-for-ios-explore-s-7heresdk14IsolineOptionsV07evTruckC0AA07EVTruckC0VSgvp">`IsolineOptions.evTruckOptions`</a> and <a href="sdk-for-ios-explore-structs-isolineoptions#sdk-for-ios-explore-s-7heresdk14IsolineOptionsV07routingC0AA07RoutingC0VSgvp">`IsolineOptions.routingOptions`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `routing_options` instead.")
  public var carOptions: CarOptions?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-caroptions">CarOptions</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14IsolineOptionsV05truckC0AA05TruckC0VSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-truckOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-isolineoptions#sdk-for-ios-explore-s-7heresdk14IsolineOptionsV05truckC0AA05TruckC0VSgvp" class="token"><code>truckOptions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies options for calculation of isolines for truck. Mutually exclusive with <a href="sdk-for-ios-explore-structs-isolineoptions#sdk-for-ios-explore-s-7heresdk14IsolineOptionsV03carC0AA03CarC0VSgvp">`IsolineOptions.carOptions`</a>, <a href="sdk-for-ios-explore-structs-isolineoptions#sdk-for-ios-explore-s-7heresdk14IsolineOptionsV05evCarC0AA05EVCarC0VSgvp">`IsolineOptions.evCarOptions`</a>, <a href="sdk-for-ios-explore-structs-isolineoptions#sdk-for-ios-explore-s-7heresdk14IsolineOptionsV07evTruckC0AA07EVTruckC0VSgvp">`IsolineOptions.evTruckOptions`</a> and <a href="sdk-for-ios-explore-structs-isolineoptions#sdk-for-ios-explore-s-7heresdk14IsolineOptionsV07routingC0AA07RoutingC0VSgvp">`IsolineOptions.routingOptions`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `routing_options` instead.")
  public var truckOptions: TruckOptions?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-truckoptions">TruckOptions</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14IsolineOptionsV05evCarC0AA05EVCarC0VSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-evCarOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-isolineoptions#sdk-for-ios-explore-s-7heresdk14IsolineOptionsV05evCarC0AA05EVCarC0VSgvp" class="token"><code>evCarOptions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies options for calculation of isolines for electric car. Mutually exclusive with <a href="sdk-for-ios-explore-structs-isolineoptions#sdk-for-ios-explore-s-7heresdk14IsolineOptionsV03carC0AA03CarC0VSgvp">`IsolineOptions.carOptions`</a>, <a href="sdk-for-ios-explore-structs-isolineoptions#sdk-for-ios-explore-s-7heresdk14IsolineOptionsV05truckC0AA05TruckC0VSgvp">`IsolineOptions.truckOptions`</a>, <a href="sdk-for-ios-explore-structs-isolineoptions#sdk-for-ios-explore-s-7heresdk14IsolineOptionsV07evTruckC0AA07EVTruckC0VSgvp">`IsolineOptions.evTruckOptions`</a> and <a href="sdk-for-ios-explore-structs-isolineoptions#sdk-for-ios-explore-s-7heresdk14IsolineOptionsV07routingC0AA07RoutingC0VSgvp">`IsolineOptions.routingOptions`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `routing_options` instead.")
  public var evCarOptions: EVCarOptions?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-evcaroptions">EVCarOptions</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14IsolineOptionsV07evTruckC0AA07EVTruckC0VSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-evTruckOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-isolineoptions#sdk-for-ios-explore-s-7heresdk14IsolineOptionsV07evTruckC0AA07EVTruckC0VSgvp" class="token"><code>evTruckOptions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies options for calculation of isolines for electric truck. Mutually exclusive with <a href="sdk-for-ios-explore-structs-isolineoptions#sdk-for-ios-explore-s-7heresdk14IsolineOptionsV03carC0AA03CarC0VSgvp">`IsolineOptions.carOptions`</a>, <a href="sdk-for-ios-explore-structs-isolineoptions#sdk-for-ios-explore-s-7heresdk14IsolineOptionsV05truckC0AA05TruckC0VSgvp">`IsolineOptions.truckOptions`</a>, <a href="sdk-for-ios-explore-structs-isolineoptions#sdk-for-ios-explore-s-7heresdk14IsolineOptionsV05evCarC0AA05EVCarC0VSgvp">`IsolineOptions.evCarOptions`</a> and <a href="sdk-for-ios-explore-structs-isolineoptions#sdk-for-ios-explore-s-7heresdk14IsolineOptionsV07routingC0AA07RoutingC0VSgvp">`IsolineOptions.routingOptions`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `routing_options` instead.")
  public var evTruckOptions: EVTruckOptions?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-evtruckoptions">EVTruckOptions</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14IsolineOptionsV07routingC0AA07RoutingC0VSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-routingOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-isolineoptions#sdk-for-ios-explore-s-7heresdk14IsolineOptionsV07routingC0AA07RoutingC0VSgvp" class="token"><code>routingOptions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies options for calculation of isolines for any vehicle type. Mutually exclusive with <a href="sdk-for-ios-explore-structs-isolineoptions#sdk-for-ios-explore-s-7heresdk14IsolineOptionsV03carC0AA03CarC0VSgvp">`IsolineOptions.carOptions`</a>, <a href="sdk-for-ios-explore-structs-isolineoptions#sdk-for-ios-explore-s-7heresdk14IsolineOptionsV05truckC0AA05TruckC0VSgvp">`IsolineOptions.truckOptions`</a>, <a href="sdk-for-ios-explore-structs-isolineoptions#sdk-for-ios-explore-s-7heresdk14IsolineOptionsV05evCarC0AA05EVCarC0VSgvp">`IsolineOptions.evCarOptions`</a> and <a href="sdk-for-ios-explore-structs-isolineoptions#sdk-for-ios-explore-s-7heresdk14IsolineOptionsV07evTruckC0AA07EVTruckC0VSgvp">`IsolineOptions.evTruckOptions`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var routingOptions: RoutingOptions?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-routingoptions">RoutingOptions</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14IsolineOptionsV011calculationC003carC0A2C11CalculationV_AA03CarC0Vtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-calculationOptions-carOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-isolineoptions#sdk-for-ios-explore-s-7heresdk14IsolineOptionsV011calculationC003carC0A2C11CalculationV_AA03CarC0Vtcfc" class="token"><code>init(calculationOptions:</code><wbr></wbr><code>carOptions:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs options to calculate isolines from destination or origin, with preferences for isoline calculation and car routing options.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the constructor with `RoutingOptions` parameter instead.")
  public init(calculationOptions: IsolineOptions.Calculation, carOptions: CarOptions)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-isolineoptions-calculation">Calculation</a>
  - <a href="sdk-for-ios-explore-structs-caroptions">CarOptions</a>

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
  <td><code> </code><em><code>calculationOptions</code></em><code> </code></td>
  <td><div>
  <p>The options to be used to calculate this isoline.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>carOptions</code></em><code> </code></td>
  <td><div>
  <p>The options that should influence the possible routes within the isoline. This determines also the transportation type.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14IsolineOptionsV011calculationC005truckC0A2C11CalculationV_AA05TruckC0Vtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-calculationOptions-truckOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-isolineoptions#sdk-for-ios-explore-s-7heresdk14IsolineOptionsV011calculationC005truckC0A2C11CalculationV_AA05TruckC0Vtcfc" class="token"><code>init(calculationOptions:</code><wbr></wbr><code>truckOptions:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs options to calculate isolines from destination or origin, with preferences for isoline calculation and truck routing options.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the constructor with `RoutingOptions` parameter instead.")
  public init(calculationOptions: IsolineOptions.Calculation, truckOptions: TruckOptions)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-isolineoptions-calculation">Calculation</a>
  - <a href="sdk-for-ios-explore-structs-truckoptions">TruckOptions</a>

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
  <td><code> </code><em><code>calculationOptions</code></em><code> </code></td>
  <td><div>
  <p>The options to be used to calculate this isoline.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>truckOptions</code></em><code> </code></td>
  <td><div>
  <p>The options that should influence the possible routes within the isoline. This determines also the transportation type.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14IsolineOptionsV011calculationC005evCarC0A2C11CalculationV_AA05EVCarC0Vtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-calculationOptions-evCarOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-isolineoptions#sdk-for-ios-explore-s-7heresdk14IsolineOptionsV011calculationC005evCarC0A2C11CalculationV_AA05EVCarC0Vtcfc" class="token"><code>init(calculationOptions:</code><wbr></wbr><code>evCarOptions:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs options to calculate isolines from destination or origin, with preferences for isoline calculation and electric car routing options.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the constructor with `RoutingOptions` parameter instead.")
  public init(calculationOptions: IsolineOptions.Calculation, evCarOptions: EVCarOptions)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-isolineoptions-calculation">Calculation</a>
  - <a href="sdk-for-ios-explore-structs-evcaroptions">EVCarOptions</a>

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
  <td><code> </code><em><code>calculationOptions</code></em><code> </code></td>
  <td><div>
  <p>The options to be used to calculate this isoline.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>evCarOptions</code></em><code> </code></td>
  <td><div>
  <p>The options that should influence the possible routes within the isoline. This determines also the transportation type.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14IsolineOptionsV011calculationC007evTruckC0A2C11CalculationV_AA07EVTruckC0Vtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-calculationOptions-evTruckOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-isolineoptions#sdk-for-ios-explore-s-7heresdk14IsolineOptionsV011calculationC007evTruckC0A2C11CalculationV_AA07EVTruckC0Vtcfc" class="token"><code>init(calculationOptions:</code><wbr></wbr><code>evTruckOptions:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs options to calculate isolines from destination or origin, with preferences for isoline calculation and electric truck routing options.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the constructor with `RoutingOptions` parameter instead.")
  public init(calculationOptions: IsolineOptions.Calculation, evTruckOptions: EVTruckOptions)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-isolineoptions-calculation">Calculation</a>
  - <a href="sdk-for-ios-explore-structs-evtruckoptions">EVTruckOptions</a>

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
  <td><code> </code><em><code>calculationOptions</code></em><code> </code></td>
  <td><div>
  <p>The options to be used to calculate this isoline.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>evTruckOptions</code></em><code> </code></td>
  <td><div>
  <p>The options that should influence the possible routes within the isoline. This determines also the transportation type.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14IsolineOptionsV011calculationC007routingC0A2C11CalculationV_AA07RoutingC0Vtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-calculationOptions-routingOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-isolineoptions#sdk-for-ios-explore-s-7heresdk14IsolineOptionsV011calculationC007routingC0A2C11CalculationV_AA07RoutingC0Vtcfc" class="token"><code>init(calculationOptions:</code><wbr></wbr><code>routingOptions:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs options to calculate isolines from destination or origin, with preferences for isoline calculation and routing options. **Notes**

  - By default all vehicle specifications from <a href="sdk-for-ios-explore-structs-routingoptions#sdk-for-ios-explore-s-7heresdk14RoutingOptionsV22transportSpecificationAA09TransportE0Vvp">`RoutingOptions.transportSpecification`</a> are set to `nil` and the <a href="sdk-for-ios-explore-structs-transportspecification#sdk-for-ios-explore-s-7heresdk22TransportSpecificationV13transportModeAA0bE0Ovp">`TransportSpecification.transportMode`</a> from <a href="sdk-for-ios-explore-structs-routingoptions#sdk-for-ios-explore-s-7heresdk14RoutingOptionsV22transportSpecificationAA09TransportE0Vvp">`RoutingOptions.transportSpecification`</a> is set to <a href="sdk-for-ios-explore-enums-transportmode#sdk-for-ios-explore-s-7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a>.
  - A route can be calculated with only the <a href="sdk-for-ios-explore-structs-transportspecification#sdk-for-ios-explore-s-7heresdk22TransportSpecificationV13transportModeAA0bE0Ovp">`TransportSpecification.transportMode`</a> from <a href="sdk-for-ios-explore-structs-routingoptions#sdk-for-ios-explore-s-7heresdk14RoutingOptionsV22transportSpecificationAA09TransportE0Vvp">`RoutingOptions.transportSpecification`</a> set.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(calculationOptions: IsolineOptions.Calculation, routingOptions: RoutingOptions)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-isolineoptions-calculation">Calculation</a>
  - <a href="sdk-for-ios-explore-structs-routingoptions">RoutingOptions</a>

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
  <td><code> </code><em><code>calculationOptions</code></em><code> </code></td>
  <td><div>
  <p>The options to be used to calculate this isoline.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>routingOptions</code></em><code> </code></td>
  <td><div>
  <p>The options that should influence the possible routes within the isoline. This determines also the transportation type.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14IsolineOptionsV11CalculationV"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Struct-Calculation" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-isolineoptions#sdk-for-ios-explore-s-7heresdk14IsolineOptionsV11CalculationV" class="token"><code>Calculation</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies isoline parameters. Setting at least one limit to <a href="sdk-for-ios-explore-structs-isolineoptions-calculation#sdk-for-ios-explore-s-7heresdk14IsolineOptionsV11CalculationV11rangeValuesSays5Int32VGvp">`IsolineOptions.Calculation.rangeValues`</a> is mandatory or the calculation will fail.

  <a href="sdk-for-ios-explore-structs-isolineoptions-calculation" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct Calculation
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

