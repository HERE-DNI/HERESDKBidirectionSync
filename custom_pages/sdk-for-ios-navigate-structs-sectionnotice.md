---
title: "SectionNotice Structure Reference"
slug: "sdk-for-ios-navigate-structs-sectionnotice"
---

# SectionNotice

<div class="declaration">

<div class="language">

``` highlight
public struct SectionNotice : Hashable
```

</div>

</div>

Explains an issue encountered in a <a href="sdk-for-ios-navigate-classes-section">`Section`</a>.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13SectionNoticeV4codeAA0bC4CodeOvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-code" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-sectionnotice#sdk-for-ios-navigate-s-7heresdk13SectionNoticeV4codeAA0bC4CodeOvp" class="token"><code>code</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The notice code.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var code: SectionNoticeCode
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-sectionnoticecode">SectionNoticeCode</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13SectionNoticeV8severityAA0C8SeverityOvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-severity" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-sectionnotice#sdk-for-ios-navigate-s-7heresdk13SectionNoticeV8severityAA0C8SeverityOvp" class="token"><code>severity</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The notice severity.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var severity: NoticeSeverity
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-noticeseverity">NoticeSeverity</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13SectionNoticeV20violatedRestrictionsSayAA19ViolatedRestrictionVGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-violatedRestrictions" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-sectionnotice#sdk-for-ios-navigate-s-7heresdk13SectionNoticeV20violatedRestrictionsSayAA19ViolatedRestrictionVGvp" class="token"><code>violatedRestrictions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The following property `violated_restrictions` contains the notice detail information. Only three types of restrictions can have notice details: time dependent restriction, vehicle restriction and transport mode restriction. There is no one-to-one match of the <a href="sdk-for-ios-navigate-structs-sectionnotice#sdk-for-ios-navigate-s-7heresdk13SectionNoticeV4codeAA0bC4CodeOvp">`SectionNotice.code`</a> and these three restriction types. For example, if <a href="sdk-for-ios-navigate-structs-sectionnotice#sdk-for-ios-navigate-s-7heresdk13SectionNoticeV4codeAA0bC4CodeOvp">`SectionNotice.code`</a> is <a href="sdk-for-ios-navigate-enums-sectionnoticecode#sdk-for-ios-navigate-s-7heresdk17SectionNoticeCodeO26violatedVehicleRestrictionyA2CmF">`SectionNoticeCode.violatedVehicleRestriction`</a>, then it can be either vehicle restriction or transport mode restriction. If <a href="sdk-for-ios-navigate-structs-sectionnotice#sdk-for-ios-navigate-s-7heresdk13SectionNoticeV4codeAA0bC4CodeOvp">`SectionNotice.code`</a> is <a href="sdk-for-ios-navigate-enums-sectionnoticecode#sdk-for-ios-navigate-s-7heresdk17SectionNoticeCodeO15seasonalClosureyA2CmF">`SectionNoticeCode.seasonalClosure`</a>, then it is time dependent restriction. If the section notice is none of the above-mentioned three types, then this will be an empty list.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var violatedRestrictions: [ViolatedRestriction]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-violatedrestriction">ViolatedRestriction</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13SectionNoticeV4code8severity20violatedRestrictionsAcA0bC4CodeO_AA0C8SeverityOSayAA19ViolatedRestrictionVGtcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-code-severity-violatedRestrictions" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-sectionnotice#sdk-for-ios-navigate-s-7heresdk13SectionNoticeV4code8severity20violatedRestrictionsAcA0bC4CodeO_AA0C8SeverityOSayAA19ViolatedRestrictionVGtcfc" class="token"><code>init(code:</code><wbr></wbr><code>severity:</code><wbr></wbr><code>violatedRestrictions:</code><wbr></wbr><code>)</code></a> 

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
  public init(code: SectionNoticeCode, severity: NoticeSeverity, violatedRestrictions: [ViolatedRestriction] = [])
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-sectionnoticecode">SectionNoticeCode</a>
  - <a href="sdk-for-ios-navigate-enums-noticeseverity">NoticeSeverity</a>
  - <a href="sdk-for-ios-navigate-structs-violatedrestriction">ViolatedRestriction</a>

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

