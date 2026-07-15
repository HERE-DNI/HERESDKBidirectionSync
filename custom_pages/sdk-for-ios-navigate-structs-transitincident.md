---
title: "TransitIncident Structure Reference"
slug: "sdk-for-ios-navigate-structs-transitincident"
---

# TransitIncident

<div class="declaration">

<div class="language">

``` highlight
public struct TransitIncident : Hashable
```

</div>

</div>

A transit incident describes disruptions on the transit network. Disruptions scale from delays to service cancellations.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk15TransitIncidentV7summarySSSgvp"></span>` `<span id="//apple_ref/swift/Property/summary" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-transitincident#/s:7heresdk15TransitIncidentV7summarySSSgvp" class="token"><code>summary</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A human readable summary of the incident.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var summary: String?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15TransitIncidentV11descriptionSSSgvp"></span>` `<span id="//apple_ref/swift/Property/description" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-transitincident#/s:7heresdk15TransitIncidentV11descriptionSSSgvp" class="token"><code>description</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A human readable description of the incident

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var description: String?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15TransitIncidentV4typeAA0bC4TypeOSgvp"></span>` `<span id="//apple_ref/swift/Property/type" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-transitincident#/s:7heresdk15TransitIncidentV4typeAA0bC4TypeOSgvp" class="token"><code>type</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Type of the incident.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var type: TransitIncidentType?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15TransitIncidentV6effectAA0bC6EffectOSgvp"></span>` `<span id="//apple_ref/swift/Property/effect" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-transitincident#/s:7heresdk15TransitIncidentV6effectAA0bC6EffectOSgvp" class="token"><code>effect</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Effect of the incident.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var effect: TransitIncidentEffect?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15TransitIncidentV9validFrom10Foundation4DateVSgvp"></span>` `<span id="//apple_ref/swift/Property/validFrom" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-transitincident#/s:7heresdk15TransitIncidentV9validFrom10Foundation4DateVSgvp" class="token"><code>validFrom</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Valid from.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var validFrom: Date?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15TransitIncidentV10validUntil10Foundation4DateVSgvp"></span>` `<span id="//apple_ref/swift/Property/validUntil" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-transitincident#/s:7heresdk15TransitIncidentV10validUntil10Foundation4DateVSgvp" class="token"><code>validUntil</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Valid until.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var validUntil: Date?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15TransitIncidentV3urlSSSgvp"></span>` `<span id="//apple_ref/swift/Property/url" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-transitincident#/s:7heresdk15TransitIncidentV3urlSSSgvp" class="token"><code>url</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Link to the original incident published at the agency website.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var url: String?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(summary: description: type: effect: validFrom: validUntil: url: )

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
  public init ( summary : String ? = nil , description : String ? = nil , type : TransitIncidentType ? = nil , effect : TransitIncidentEffect ? = nil , validFrom : Date ? = nil , validUntil : Date ? = nil , url : String ? = nil )
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

