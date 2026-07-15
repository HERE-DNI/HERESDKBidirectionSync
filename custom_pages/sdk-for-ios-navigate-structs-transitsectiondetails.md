---
title: "TransitSectionDetails Structure Reference"
slug: "sdk-for-ios-navigate-structs-transitsectiondetails"
---

# TransitSectionDetails

<div class="declaration">

<div class="language">

``` highlight
public struct TransitSectionDetails : Hashable
```

</div>

</div>

Gives the details of a transit section.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk21TransitSectionDetailsV9transportAA0B9TransportVSgvp"></span>` `<span id="//apple_ref/swift/Property/transport" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-transitsectiondetails#/s:7heresdk21TransitSectionDetailsV9transportAA0B9TransportVSgvp" class="token"><code>transport</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Transit transport information.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var transport: TransitTransport?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21TransitSectionDetailsV17intermediateStopsSayAA0B4StopVGvp"></span>` `<span id="//apple_ref/swift/Property/intermediateStops" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-transitsectiondetails#/s:7heresdk21TransitSectionDetailsV17intermediateStopsSayAA0B4StopVGvp" class="token"><code>intermediateStops</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  All the intermediate stops between departure and destination of this section.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var intermediateStops: [TransitStop]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21TransitSectionDetailsV6agencyAA6AgencyVvp"></span>` `<span id="//apple_ref/swift/Property/agency" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-transitsectiondetails#/s:7heresdk21TransitSectionDetailsV6agencyAA6AgencyVvp" class="token"><code>agency</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Contains information about a particular agency.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var agency: Agency
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21TransitSectionDetailsV12attributionsSayAA11AttributionVGvp"></span>` `<span id="//apple_ref/swift/Property/attributions" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-transitsectiondetails#/s:7heresdk21TransitSectionDetailsV12attributionsSayAA11AttributionVGvp" class="token"><code>attributions</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of required attributions to display.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var attributions: [Attribution]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21TransitSectionDetailsV5faresSayAA4FareVGvp"></span>` `<span id="//apple_ref/swift/Property/fares" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-transitsectiondetails#/s:7heresdk21TransitSectionDetailsV5faresSayAA4FareVGvp" class="token"><code>fares</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of tickets to pay for this section of the route.

  **Note:** Currently, fare information is not supported and the list will be always empty.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var fares: [Fare]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21TransitSectionDetailsV9incidentsSayAA0B8IncidentVGvp"></span>` `<span id="//apple_ref/swift/Property/incidents" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-transitsectiondetails#/s:7heresdk21TransitSectionDetailsV9incidentsSayAA0B8IncidentVGvp" class="token"><code>incidents</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A list of all incidents that apply to the section.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var incidents: [TransitIncident]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(transport: intermediateStops: agency: attributions: fares: incidents: )

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

    - transport: Transit transport information.
    - intermediateStops: All the intermediate stops between departure and destination of this section.
    - agency: Contains information about a particular agency.
    - attributions: List of required attributions to display.
    - fares: List of tickets to pay for this section of the route.

    **Note:** Currently, fare information is not supported and the list will be always empty.

    - incidents: A list of all incidents that apply to the section.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( transport : TransitTransport ? = nil , intermediateStops : [ TransitStop ] = [], agency : Agency , attributions : [ Attribution ] = [], fares : [ Fare ] = [], incidents : [ TransitIncident ] = [])
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

