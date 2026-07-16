---
title: "RoadShieldIconProperties Structure Reference"
slug: "sdk-for-ios-explore-structs-roadshieldiconproperties"
---

# RoadShieldIconProperties

<div class="declaration">

<div class="language">

``` highlight
public struct RoadShieldIconProperties
```

</div>

</div>

Contains the information required to create a road shield image.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk24RoadShieldIconPropertiesV9routeTypeAA05RouteG0Ovp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-routeType" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-roadshieldiconproperties#sdk-for-ios-explore-s-7heresdk24RoadShieldIconPropertiesV9routeTypeAA05RouteG0Ovp" class="token"><code>routeType</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The type of route indicating the significance of the road in a range from 0 to 6. A value of 1 stands for the most major route and 6 the most minor, with 0 being of unknown type.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var routeType: RouteType
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-routetype">RouteType</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk24RoadShieldIconPropertiesV11countryCodeSSvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-countryCode" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-roadshieldiconproperties#sdk-for-ios-explore-s-7heresdk24RoadShieldIconPropertiesV11countryCodeSSvp" class="token"><code>countryCode</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The country code in ISO-3166-1 alpha-3 format, which will determine the type of road shield.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var countryCode: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk24RoadShieldIconPropertiesV9stateCodeSSvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-stateCode" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-roadshieldiconproperties#sdk-for-ios-explore-s-7heresdk24RoadShieldIconPropertiesV9stateCodeSSvp" class="token"><code>stateCode</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The state code for the road. It’s a 2-letter code in ISO 3166-2 format. For example the ones listed for US on this page <https://en.wikipedia.org/wiki/ISO_3166-2:US>. The code “AL” is for Alabama. Another example is the code for autonomous communities listed on <https://en.wikipedia.org/wiki/ISO_3166-2:ES>. Can be empty if not required for the particular country.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var stateCode: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk24RoadShieldIconPropertiesV15routeNumberNameSSvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-routeNumberName" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-roadshieldiconproperties#sdk-for-ios-explore-s-7heresdk24RoadShieldIconPropertiesV15routeNumberNameSSvp" class="token"><code>routeNumberName</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A string that is used to additionally determine the road shield’s visual representation. In a routing context, the text can be taken from a <a href="sdk-for-ios-explore-structs-localizedroadnumber">`LocalizedRoadNumber`</a>, which is available for each <a href="sdk-for-ios-explore-classes-span">`Span`</a> of a <a href="sdk-for-ios-explore-classes-route">`Route`</a> object. Typically, the string contains the number of a road, such as “E100”. Internally, the text is parsed with a RegEx pattern and the results will be used along with other properties such as <a href="sdk-for-ios-explore-structs-roadshieldiconproperties#sdk-for-ios-explore-s-7heresdk24RoadShieldIconPropertiesV9routeTypeAA05RouteG0Ovp">`routeType`</a>, <a href="sdk-for-ios-explore-structs-roadshieldiconproperties#sdk-for-ios-explore-s-7heresdk24RoadShieldIconPropertiesV11countryCodeSSvp">`countryCode`</a> and <a href="sdk-for-ios-explore-structs-roadshieldiconproperties#sdk-for-ios-explore-s-7heresdk24RoadShieldIconPropertiesV9stateCodeSSvp">`stateCode`</a> to identify the visual representation of a road shield icon.

  Note that the actual text which will be displayed on the road shield icon is set with <a href="sdk-for-ios-explore-structs-roadshieldiconproperties#sdk-for-ios-explore-s-7heresdk24RoadShieldIconPropertiesV10shieldTextSSvp">`RoadShieldIconProperties.shieldText`</a>. In order to determine the visuals of the icon, <a href="sdk-for-ios-explore-structs-roadshieldiconproperties#sdk-for-ios-explore-s-7heresdk24RoadShieldIconPropertiesV11countryCodeSSvp">`countryCode`</a>, <a href="sdk-for-ios-explore-structs-roadshieldiconproperties#sdk-for-ios-explore-s-7heresdk24RoadShieldIconPropertiesV9routeTypeAA05RouteG0Ovp">`routeType`</a> and eventually the <a href="sdk-for-ios-explore-structs-roadshieldiconproperties#sdk-for-ios-explore-s-7heresdk24RoadShieldIconPropertiesV9stateCodeSSvp">`stateCode`</a> is in most cases sufficient to determine the type of road shield. In this case an empty string should be passed.

  **Note:** Texts that contain a <a href="sdk-for-ios-explore-enums-cardinaldirection">`CardinalDirection`</a> are currently not supported and may lead to unexpected results. See <a href="sdk-for-ios-explore-structs-localizedroadnumber">`LocalizedRoadNumber`</a> for more details, it provides texts with and without a cardinal direction.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var routeNumberName: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk24RoadShieldIconPropertiesV10shieldTextSSvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-shieldText" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-roadshieldiconproperties#sdk-for-ios-explore-s-7heresdk24RoadShieldIconPropertiesV10shieldTextSSvp" class="token"><code>shieldText</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The text of the road-shield. This is the text which is displayed on the road-shield in reality. It will be in the output road-shield icon.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var shieldText: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk24RoadShieldIconPropertiesV9routeType11countryCode05stateI00F10NumberName10shieldTextAcA05RouteG0O_S4Stcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-routeType-countryCode-stateCode-routeNumberName-shieldText" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-roadshieldiconproperties#sdk-for-ios-explore-s-7heresdk24RoadShieldIconPropertiesV9routeType11countryCode05stateI00F10NumberName10shieldTextAcA05RouteG0O_S4Stcfc" class="token"><code>init(routeType:</code><wbr></wbr><code>countryCode:</code><wbr></wbr><code>stateCode:</code><wbr></wbr><code>routeNumberName:</code><wbr></wbr><code>shieldText:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance.

  - Parameters

    - routeType: The type of route indicating the significance of the road in a range from 0 to 6. A value of 1 stands for the most major route and 6 the most minor, with 0 being of unknown type.
    - countryCode: The country code in ISO-3166-1 alpha-3 format, which will determine the type of road shield.
    - stateCode: The state code for the road. It’s a 2-letter code in ISO 3166-2 format. For example the ones listed for US on this page <https://en.wikipedia.org/wiki/ISO_3166-2:US>. The code “AL” is for Alabama. Another example is the code for autonomous communities listed on <https://en.wikipedia.org/wiki/ISO_3166-2:ES>. Can be empty if not required for the particular country.
    - routeNumberName: A string that is used to additionally determine the road shield’s visual representation. In a routing context, the text can be taken from a <a href="sdk-for-ios-explore-structs-localizedroadnumber">`LocalizedRoadNumber`</a>, which is available for each <a href="sdk-for-ios-explore-classes-span">`Span`</a> of a <a href="sdk-for-ios-explore-classes-route">`Route`</a> object. Typically, the string contains the number of a road, such as “E100”. Internally, the text is parsed with a RegEx pattern and the results will be used along with other properties such as <a href="sdk-for-ios-explore-structs-roadshieldiconproperties#sdk-for-ios-explore-s-7heresdk24RoadShieldIconPropertiesV9routeTypeAA05RouteG0Ovp">`routeType`</a>, <a href="sdk-for-ios-explore-structs-roadshieldiconproperties#sdk-for-ios-explore-s-7heresdk24RoadShieldIconPropertiesV11countryCodeSSvp">`countryCode`</a> and <a href="sdk-for-ios-explore-structs-roadshieldiconproperties#sdk-for-ios-explore-s-7heresdk24RoadShieldIconPropertiesV9stateCodeSSvp">`stateCode`</a> to identify the visual representation of a road shield icon.

    Note that the actual text which will be displayed on the road shield icon is set with <a href="sdk-for-ios-explore-structs-roadshieldiconproperties#sdk-for-ios-explore-s-7heresdk24RoadShieldIconPropertiesV10shieldTextSSvp">`RoadShieldIconProperties.shieldText`</a>. In order to determine the visuals of the icon, <a href="sdk-for-ios-explore-structs-roadshieldiconproperties#sdk-for-ios-explore-s-7heresdk24RoadShieldIconPropertiesV11countryCodeSSvp">`countryCode`</a>, <a href="sdk-for-ios-explore-structs-roadshieldiconproperties#sdk-for-ios-explore-s-7heresdk24RoadShieldIconPropertiesV9routeTypeAA05RouteG0Ovp">`routeType`</a> and eventually the <a href="sdk-for-ios-explore-structs-roadshieldiconproperties#sdk-for-ios-explore-s-7heresdk24RoadShieldIconPropertiesV9stateCodeSSvp">`stateCode`</a> is in most cases sufficient to determine the type of road shield. In this case an empty string should be passed.

    **Note:** Texts that contain a <a href="sdk-for-ios-explore-enums-cardinaldirection">`CardinalDirection`</a> are currently not supported and may lead to unexpected results. See <a href="sdk-for-ios-explore-structs-localizedroadnumber">`LocalizedRoadNumber`</a> for more details, it provides texts with and without a cardinal direction.

    - shieldText: The text of the road-shield. This is the text which is displayed on the road-shield in reality. It will be in the output road-shield icon.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(routeType: RouteType, countryCode: String, stateCode: String, routeNumberName: String, shieldText: String)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-routetype">RouteType</a>

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

