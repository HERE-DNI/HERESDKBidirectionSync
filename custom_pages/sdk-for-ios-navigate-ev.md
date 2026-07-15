---
title: "EV  Reference"
slug: "sdk-for-ios-navigate-ev"
---

# EV

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk25EVChargingConnectorFormatO"></span>` `<span id="//apple_ref/swift/Enum/EVChargingConnectorFormat" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-ev#/s:7heresdk25EVChargingConnectorFormatO" class="token"><code>EVChargingConnectorFormat</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the format of the connector, whether it is a socket or a cable. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-enums-evchargingconnectorformat" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum EVChargingConnectorFormat : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk23EVChargingConnectorTypeV"></span>` `<span id="//apple_ref/swift/Struct/EVChargingConnectorType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-ev#/s:7heresdk23EVChargingConnectorTypeV" class="token"><code>EVChargingConnectorType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the standardized type of the installed connector. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-structs-evchargingconnectortype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct EVChargingConnectorType
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14EVSECapabilityO"></span>` `<span id="//apple_ref/swift/Enum/EVSECapability" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-ev#/s:7heresdk14EVSECapabilityO" class="token"><code>EVSECapability</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the administrative functionality that an EVSE is capable of. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-enums-evsecapability" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum EVSECapability : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18EVSEPaymentSupportO"></span>` `<span id="//apple_ref/swift/Enum/EVSEPaymentSupport" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-ev#/s:7heresdk18EVSEPaymentSupportO" class="token"><code>EVSEPaymentSupport</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the payment support functionality on EVSE for ad-hoc customers (without pre-registration). **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-enums-evsepaymentsupport" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum EVSEPaymentSupport : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9EVSEStateO"></span>` `<span id="//apple_ref/swift/Enum/EVSEState" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-ev#/s:7heresdk9EVSEStateO" class="token"><code>EVSEState</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates the current short-term status of the EVSE at the time given in the modified property. There are no separate statuses available for individual connectors. A single EVSE can only be used by a single car, so same statuses apply to other connectors as well. So, if one connector is in use, the whole EVSE has status charging, and other connectors cannot be used at the same time, hence they should be considered in-use as well. If an EVSE can allow multiple connectors to be used at the same time, it is basically multiple EVSEs merged into a single physical box or device.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-enums-evsestate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum EVSEState : UInt32, CaseIterable, Codable
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

