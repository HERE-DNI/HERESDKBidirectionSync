---
title: "EnergyMix Structure Reference"
slug: "sdk-for-ios-navigate-structs-energymix"
---

# EnergyMix

<div class="declaration">

<div class="language">

``` highlight
public struct EnergyMix : Hashable
```

</div>

</div>

Represents details on the energy supplied at the charging location. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk9EnergyMixV07isGreenB0Sbvp"></span>` `<span id="//apple_ref/swift/Property/isGreenEnergy" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-energymix#/s:7heresdk9EnergyMixV07isGreenB0Sbvp" class="token"><code>isGreenEnergy</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Boolean flag indicating if the energy is 100% from regenerative sources.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isGreenEnergy: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9EnergyMixV13energySourcesSayAA0B6SourceVGvp"></span>` `<span id="//apple_ref/swift/Property/energySources" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-energymix#/s:7heresdk9EnergyMixV13energySourcesSayAA0B6SourceVGvp" class="token"><code>energySources</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of energy sources. The sum of the percentages over the energy sources should be 100%.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var energySources: [EnergySource]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9EnergyMixV8supplierSSSgvp"></span>` `<span id="//apple_ref/swift/Property/supplier" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-energymix#/s:7heresdk9EnergyMixV8supplierSSSgvp" class="token"><code>supplier</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Name of the energy supplier.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var supplier: String?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9EnergyMixV13energyProductSSSgvp"></span>` `<span id="//apple_ref/swift/Property/energyProduct" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-energymix#/s:7heresdk9EnergyMixV13energyProductSSSgvp" class="token"><code>energyProduct</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Name of the energy suppliers product or plan.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var energyProduct: String?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9EnergyMixV20environmentalImpactsSayAA19EnvironmentalImpactVGvp"></span>` `<span id="//apple_ref/swift/Property/environmentalImpacts" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-energymix#/s:7heresdk9EnergyMixV20environmentalImpactsSayAA19EnvironmentalImpactVGvp" class="token"><code>environmentalImpacts</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of environmental impacts from this energy mix.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var environmentalImpacts: [EnvironmentalImpact]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(isGreenEnergy: energySources: supplier: energyProduct: environmentalImpacts: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( isGreenEnergy : Bool = false , energySources : [ EnergySource ] = [], supplier : String ? = nil , energyProduct : String ? = nil , environmentalImpacts : [ EnvironmentalImpact ] = [])
  ```

  </pre>

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

