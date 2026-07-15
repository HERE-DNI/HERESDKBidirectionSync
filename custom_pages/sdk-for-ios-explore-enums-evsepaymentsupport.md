---
title: "EVSEPaymentSupport Enumeration Reference"
slug: "sdk-for-ios-explore-enums-evsepaymentsupport"
---

# EVSEPaymentSupport

<div class="declaration">

<div class="language">

``` highlight
public enum EVSEPaymentSupport : UInt32, CaseIterable, Codable
```

</div>

</div>

Represents the payment support functionality on EVSE for ad-hoc customers (without pre-registration). **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk18EVSEPaymentSupportO8chipCardyA2CmF"></span>` `<span id="//apple_ref/swift/Element/chipCard" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-enums-evsepaymentsupport#/s:7heresdk18EVSEPaymentSupportO8chipCardyA2CmF" class="token"><code>chipCard</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  EVSE has a payment terminal that supports chip cards.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case chipCard
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18EVSEPaymentSupportO15contactlessCardyA2CmF"></span>` `<span id="//apple_ref/swift/Element/contactlessCard" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-enums-evsepaymentsupport#/s:7heresdk18EVSEPaymentSupportO15contactlessCardyA2CmF" class="token"><code>contactlessCard</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  EVSE has a payment terminal that supports contactless cards.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case contactlessCard
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18EVSEPaymentSupportO10creditCardyA2CmF"></span>` `<span id="//apple_ref/swift/Element/creditCard" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-enums-evsepaymentsupport#/s:7heresdk18EVSEPaymentSupportO10creditCardyA2CmF" class="token"><code>creditCard</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  EVSE has a payment terminal that makes it possible to pay for charging using a credit card.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case creditCard
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18EVSEPaymentSupportO9debitCardyA2CmF"></span>` `<span id="//apple_ref/swift/Element/debitCard" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-enums-evsepaymentsupport#/s:7heresdk18EVSEPaymentSupportO9debitCardyA2CmF" class="token"><code>debitCard</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  EVSE has a payment terminal that makes it possible to pay for charging using a debit card.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case debitCard
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18EVSEPaymentSupportO11pedTerminalyA2CmF"></span>` `<span id="//apple_ref/swift/Element/pedTerminal" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-enums-evsepaymentsupport#/s:7heresdk18EVSEPaymentSupportO11pedTerminalyA2CmF" class="token"><code>pedTerminal</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  EVSE has a payment terminal with a pin-code entry device.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case pedTerminal
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18EVSEPaymentSupportO10rfidReaderyA2CmF"></span>` `<span id="//apple_ref/swift/Element/rfidReader" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-enums-evsepaymentsupport#/s:7heresdk18EVSEPaymentSupportO10rfidReaderyA2CmF" class="token"><code>rfidReader</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Charging at this EVSE can be authorized with an RFID token.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case rfidReader
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18EVSEPaymentSupportO22authByCarPlugAndChargeyA2CmF"></span>` `<span id="//apple_ref/swift/Element/authByCarPlugAndCharge" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-enums-evsepaymentsupport#/s:7heresdk18EVSEPaymentSupportO22authByCarPlugAndChargeyA2CmF" class="token"><code>authByCarPlugAndCharge</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  ISO 15118 Plug&Charge enables drivers to plug in and charge up instantly using automatic EV-to-charging station authentication technology.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case authByCarPlugAndCharge
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18EVSEPaymentSupportO19authByCarAutochargeyA2CmF"></span>` `<span id="//apple_ref/swift/Element/authByCarAutocharge" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-enums-evsepaymentsupport#/s:7heresdk18EVSEPaymentSupportO19authByCarAutochargeyA2CmF" class="token"><code>authByCarAutocharge</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Autocharge enables drivers to plug in and charge up instantly using automatic EV-to-charging station authentication technology.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case authByCarAutocharge
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18EVSEPaymentSupportO14onlineApplePayyA2CmF"></span>` `<span id="//apple_ref/swift/Element/onlineApplePay" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-enums-evsepaymentsupport#/s:7heresdk18EVSEPaymentSupportO14onlineApplePayyA2CmF" class="token"><code>onlineApplePay</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Authenticate & pay with Apple Pay.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case onlineApplePay
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18EVSEPaymentSupportO12onlinePaypalyA2CmF"></span>` `<span id="//apple_ref/swift/Element/onlinePaypal" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-enums-evsepaymentsupport#/s:7heresdk18EVSEPaymentSupportO12onlinePaypalyA2CmF" class="token"><code>onlinePaypal</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Authenticate & pay with PayPal.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case onlinePaypal
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18EVSEPaymentSupportO16onlineCreditCardyA2CmF"></span>` `<span id="//apple_ref/swift/Element/onlineCreditCard" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-enums-evsepaymentsupport#/s:7heresdk18EVSEPaymentSupportO16onlineCreditCardyA2CmF" class="token"><code>onlineCreditCard</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Authenticate & pay with credit card online.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case onlineCreditCard
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18EVSEPaymentSupportO15onlineGooglePayyA2CmF"></span>` `<span id="//apple_ref/swift/Element/onlineGooglePay" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-enums-evsepaymentsupport#/s:7heresdk18EVSEPaymentSupportO15onlineGooglePayyA2CmF" class="token"><code>onlineGooglePay</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Authenticate & pay with Google Pay.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case onlineGooglePay
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18EVSEPaymentSupportO17onlineBankPaymentyA2CmF"></span>` `<span id="//apple_ref/swift/Element/onlineBankPayment" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-enums-evsepaymentsupport#/s:7heresdk18EVSEPaymentSupportO17onlineBankPaymentyA2CmF" class="token"><code>onlineBankPayment</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Authenticate & pay with online bank payment.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case onlineBankPayment
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18EVSEPaymentSupportO14terminalQrCodeyA2CmF"></span>` `<span id="//apple_ref/swift/Element/terminalQrCode" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-enums-evsepaymentsupport#/s:7heresdk18EVSEPaymentSupportO14terminalQrCodeyA2CmF" class="token"><code>terminalQrCode</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Initiate authentication & payment with QR code on the terminal.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case terminalQrCode
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18EVSEPaymentSupportO11terminalSmsyA2CmF"></span>` `<span id="//apple_ref/swift/Element/terminalSms" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-enums-evsepaymentsupport#/s:7heresdk18EVSEPaymentSupportO11terminalSmsyA2CmF" class="token"><code>terminalSms</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Authenticate & pay with SMS on the terminal.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case terminalSms
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18EVSEPaymentSupportO11operatorAppyA2CmF"></span>` `<span id="//apple_ref/swift/Element/operatorApp" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-enums-evsepaymentsupport#/s:7heresdk18EVSEPaymentSupportO11operatorAppyA2CmF" class="token"><code>operatorApp</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Authenticate & pay with charge point operator application on mobile phone.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case operatorApp
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18EVSEPaymentSupportO13mobilePaymentyA2CmF"></span>` `<span id="//apple_ref/swift/Element/mobilePayment" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-enums-evsepaymentsupport#/s:7heresdk18EVSEPaymentSupportO13mobilePaymentyA2CmF" class="token"><code>mobilePayment</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Used with <a href="sdk-for-ios-explore-enums-evsepaymentsupport#/s:7heresdk18EVSEPaymentSupportO11operatorAppyA2CmF">`EVSEPaymentSupport.operatorApp`</a>, <a href="sdk-for-ios-explore-enums-evsepaymentsupport#/s:7heresdk18EVSEPaymentSupportO14onlineApplePayyA2CmF">`EVSEPaymentSupport.onlineApplePay`</a>, <a href="sdk-for-ios-explore-enums-evsepaymentsupport#/s:7heresdk18EVSEPaymentSupportO12onlinePaypalyA2CmF">`EVSEPaymentSupport.onlinePaypal`</a>, <a href="sdk-for-ios-explore-enums-evsepaymentsupport#/s:7heresdk18EVSEPaymentSupportO16onlineCreditCardyA2CmF">`EVSEPaymentSupport.onlineCreditCard`</a>, <a href="sdk-for-ios-explore-enums-evsepaymentsupport#/s:7heresdk18EVSEPaymentSupportO15onlineGooglePayyA2CmF">`EVSEPaymentSupport.onlineGooglePay`</a>, <a href="sdk-for-ios-explore-enums-evsepaymentsupport#/s:7heresdk18EVSEPaymentSupportO17onlineBankPaymentyA2CmF">`EVSEPaymentSupport.onlineBankPayment`</a>, <a href="sdk-for-ios-explore-enums-evsepaymentsupport#/s:7heresdk18EVSEPaymentSupportO11terminalSmsyA2CmF">`EVSEPaymentSupport.terminalSms`</a>, <a href="sdk-for-ios-explore-enums-evsepaymentsupport#/s:7heresdk18EVSEPaymentSupportO14terminalQrCodeyA2CmF">`EVSEPaymentSupport.terminalQrCode`</a>, and <a href="sdk-for-ios-explore-enums-evsepaymentsupport#/s:7heresdk18EVSEPaymentSupportO15contactlessCardyA2CmF">`EVSEPaymentSupport.contactlessCard`</a>. Whenever one or more of those payment types is specified, `EVSEPaymentSupport.mobilePayment` is also specified.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case mobilePayment
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

