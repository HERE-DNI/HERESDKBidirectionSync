---
title: "TaxiBuilder Class Reference"
slug: "sdk-for-ios-explore-structs-transportspecification-taxibuilder"
---

# TaxiBuilder

<div class="declaration">

<div class="language">

``` highlight
public class TaxiBuilder
```

``` highlight
extension TransportSpecification.TaxiBuilder: NativeBase
```

``` highlight
extension TransportSpecification.TaxiBuilder: Hashable
```

</div>

Related types:

- <a href="sdk-for-ios-explore-structs-transportspecification">TransportSpecification</a>

</div>

This class constructs a <a href="sdk-for-ios-explore-structs-transportspecification">`TransportSpecification`</a> for a taxi.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk22TransportSpecificationV11TaxiBuilderCAEycfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-transportspecification-taxibuilder#sdk-for-ios-explore-s-7heresdk22TransportSpecificationV11TaxiBuilderCAEycfc" class="token"><code>init()</code></a> 

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
  public init()
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk22TransportSpecificationV11TaxiBuilderC04withdC0yAeA0dC0VF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-withTaxiSpecification-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-transportspecification-taxibuilder#sdk-for-ios-explore-s-7heresdk22TransportSpecificationV11TaxiBuilderC04withdC0yAeA0dC0VF" class="token"><code>withTaxiSpecification(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the taxi specification.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func withTaxiSpecification(_ taxiSpecification: TaxiSpecification) -> TransportSpecification.TaxiBuilder
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-taxispecification">TaxiSpecification</a>
  - <a href="sdk-for-ios-explore-structs-transportspecification">TransportSpecification</a>

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
  <td><code> </code><em><code>taxiSpecification</code></em><code> </code></td>
  <td><div>
  <p>The taxi specification.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The `TransportSpecification.TaxiBuilder` object with the taxi specification set to the new value.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk22TransportSpecificationV11TaxiBuilderC011withVehicleC0yAeA0gC0VF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-withVehicleSpecification-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-transportspecification-taxibuilder#sdk-for-ios-explore-s-7heresdk22TransportSpecificationV11TaxiBuilderC011withVehicleC0yAeA0gC0VF" class="token"><code>withVehicleSpecification(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the vehicle specification.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func withVehicleSpecification(_ vehicleSpecification: VehicleSpecification) -> TransportSpecification.TaxiBuilder
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-vehiclespecification">VehicleSpecification</a>
  - <a href="sdk-for-ios-explore-structs-transportspecification">TransportSpecification</a>

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
  <td><code> </code><em><code>vehicleSpecification</code></em><code> </code></td>
  <td><div>
  <p>The vehicle specification.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The `TransportSpecification.TaxiBuilder` object with the vehicle specification set to the new value.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk22TransportSpecificationV11TaxiBuilderC5buildACyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-build" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-transportspecification-taxibuilder#sdk-for-ios-explore-s-7heresdk22TransportSpecificationV11TaxiBuilderC5buildACyF" class="token"><code>build()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Builds the <a href="sdk-for-ios-explore-structs-transportspecification">`TransportSpecification`</a> object for a taxi with the specifications taken from the `TransportSpecification.TaxiBuilder` object.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func build() -> TransportSpecification
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-transportspecification">TransportSpecification</a>

  </div>

  <div>

  #### Return Value

  The <a href="sdk-for-ios-explore-structs-transportspecification">`TransportSpecification`</a> object created from the `TransportSpecification.TaxiBuilder` object.

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

