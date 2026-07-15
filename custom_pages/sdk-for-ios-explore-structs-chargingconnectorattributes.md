---
title: "ChargingConnectorAttributes Structure Reference"
slug: "sdk-for-ios-explore-structs-chargingconnectorattributes"
---

# ChargingConnectorAttributes

<div class="declaration">

<div class="language">

``` highlight
public struct ChargingConnectorAttributes : Hashable
```

</div>

</div>

Details of the connector that is suggested to be used in the section’s <a href="sdk-for-ios-explore-structs-postaction">`PostAction`</a>‘s for charging.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk27ChargingConnectorAttributesV16powerInKilowattsSdvp"></span>` `<span id="//apple_ref/swift/Property/powerInKilowatts" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-chargingconnectorattributes#/s:7heresdk27ChargingConnectorAttributesV16powerInKilowattsSdvp" class="token"><code>powerInKilowatts</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Power supplied by the suggested connector in kW.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var powerInKilowatts: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk27ChargingConnectorAttributesV16currentInAmperesSdSgvp"></span>` `<span id="//apple_ref/swift/Property/currentInAmperes" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-chargingconnectorattributes#/s:7heresdk27ChargingConnectorAttributesV16currentInAmperesSdSgvp" class="token"><code>currentInAmperes</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Current of the suggested connector in Amperes.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var currentInAmperes: Double?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk27ChargingConnectorAttributesV14voltageInVoltsSdSgvp"></span>` `<span id="//apple_ref/swift/Property/voltageInVolts" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-chargingconnectorattributes#/s:7heresdk27ChargingConnectorAttributesV14voltageInVoltsSdSgvp" class="token"><code>voltageInVolts</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Voltage of the suggested connector in Volts.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var voltageInVolts: Double?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk27ChargingConnectorAttributesV10supplyTypeAA0b6SupplyF0OSgvp"></span>` `<span id="//apple_ref/swift/Property/supplyType" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-chargingconnectorattributes#/s:7heresdk27ChargingConnectorAttributesV10supplyTypeAA0b6SupplyF0OSgvp" class="token"><code>supplyType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Supply type of the suggested connector.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var supplyType: ChargingSupplyType?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk27ChargingConnectorAttributesV13connectorTypeAA0bcF0OSgvp"></span>` `<span id="//apple_ref/swift/Property/connectorType" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-chargingconnectorattributes#/s:7heresdk27ChargingConnectorAttributesV13connectorTypeAA0bcF0OSgvp" class="token"><code>connectorType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Suggested connector for charging at this station.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var connectorType: ChargingConnectorType?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(powerInKilowatts: currentInAmperes: voltageInVolts: supplyType: connectorType: )

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
  public init ( powerInKilowatts : Double , currentInAmperes : Double ? = nil , voltageInVolts : Double ? = nil , supplyType : ChargingSupplyType ? = nil , connectorType : ChargingConnectorType ? = nil )
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

