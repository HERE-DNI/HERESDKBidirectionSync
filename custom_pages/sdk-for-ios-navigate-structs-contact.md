---
title: "Contact Structure Reference"
slug: "sdk-for-ios-navigate-structs-contact"
---

# Contact

<div class="declaration">

<div class="language">

``` highlight
public struct Contact : Hashable
```

</div>

</div>

Represents contact information.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7ContactV14landlinePhonesSayAA13LandlinePhoneVGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-landlinePhones" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-contact#sdk-for-ios-navigate-s-7heresdk7ContactV14landlinePhonesSayAA13LandlinePhoneVGvp" class="token"><code>landlinePhones</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of landline phone numbers with associated categories. This data is not available in offline search.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var landlinePhones: [LandlinePhone]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-landlinephone">LandlinePhone</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7ContactV12mobilePhonesSayAA11MobilePhoneVGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-mobilePhones" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-contact#sdk-for-ios-navigate-s-7heresdk7ContactV12mobilePhonesSayAA11MobilePhoneVGvp" class="token"><code>mobilePhones</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of mobile phones numbers with associated categories. This data is not available in offline search.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var mobilePhones: [MobilePhone]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-mobilephone">MobilePhone</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7ContactV6emailsSayAA12EmailAddressVGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-emails" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-contact#sdk-for-ios-navigate-s-7heresdk7ContactV6emailsSayAA12EmailAddressVGvp" class="token"><code>emails</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of email addresses with associated categories. This data is not available in offline search.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var emails: [EmailAddress]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-emailaddress">EmailAddress</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7ContactV8websitesSayAA14WebsiteAddressVGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-websites" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-contact#sdk-for-ios-navigate-s-7heresdk7ContactV8websitesSayAA14WebsiteAddressVGvp" class="token"><code>websites</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of website addresses with associated categories. This data is not available in offline search.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var websites: [WebsiteAddress]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-websiteaddress">WebsiteAddress</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7ContactVACycfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-contact#sdk-for-ios-navigate-s-7heresdk7ContactVACycfc" class="token"><code>init()</code></a> 

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
  public init()
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7ContactV14landlinePhones06mobileD06emails8websitesACSayAA13LandlinePhoneVG_SayAA06MobileI0VGSayAA12EmailAddressVGSayAA07WebsiteL0VGtcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-landlinePhones-mobilePhones-emails-websites" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-contact#sdk-for-ios-navigate-s-7heresdk7ContactV14landlinePhones06mobileD06emails8websitesACSayAA13LandlinePhoneVG_SayAA06MobileI0VGSayAA12EmailAddressVGSayAA07WebsiteL0VGtcfc" class="token"><code>init(landlinePhones:</code><wbr></wbr><code>mobilePhones:</code><wbr></wbr><code>emails:</code><wbr></wbr><code>websites:</code><wbr></wbr><code>)</code></a> 

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
  public init(landlinePhones: [LandlinePhone], mobilePhones: [MobilePhone], emails: [EmailAddress], websites: [WebsiteAddress])
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-landlinephone">LandlinePhone</a>
  - <a href="sdk-for-ios-navigate-structs-mobilephone">MobilePhone</a>
  - <a href="sdk-for-ios-navigate-structs-emailaddress">EmailAddress</a>
  - <a href="sdk-for-ios-navigate-structs-websiteaddress">WebsiteAddress</a>

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

