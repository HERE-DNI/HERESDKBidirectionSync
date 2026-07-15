---
title: "TrafficIncidentsQueryOptions Structure Reference"
slug: "sdk-for-ios-navigate-structs-trafficincidentsqueryoptions"
---

# TrafficIncidentsQueryOptions

<div class="declaration">

<div class="language">

``` highlight
public struct TrafficIncidentsQueryOptions : Hashable
```

</div>

</div>

The options to specify how incidents should be queried.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk28TrafficIncidentsQueryOptionsV10typeFilterSayAA0B12IncidentTypeOGvp"></span>` `<span id="//apple_ref/swift/Property/typeFilter" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-trafficincidentsqueryoptions#/s:7heresdk28TrafficIncidentsQueryOptionsV10typeFilterSayAA0B12IncidentTypeOGvp" class="token"><code>typeFilter</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of incident types to be queried. If the list is empty, all types will be queried.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var typeFilter: [TrafficIncidentType]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk28TrafficIncidentsQueryOptionsV12impactFilterSayAA0B14IncidentImpactOGvp"></span>` `<span id="//apple_ref/swift/Property/impactFilter" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-trafficincidentsqueryoptions#/s:7heresdk28TrafficIncidentsQueryOptionsV12impactFilterSayAA0B14IncidentImpactOGvp" class="token"><code>impactFilter</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of incident impacts to be queried. If the list is empty, all incident impacts will be queried.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var impactFilter: [TrafficIncidentImpact]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk28TrafficIncidentsQueryOptionsV17earliestStartTime10Foundation4DateVSgvp"></span>` `<span id="//apple_ref/swift/Property/earliestStartTime" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-trafficincidentsqueryoptions#/s:7heresdk28TrafficIncidentsQueryOptionsV17earliestStartTime10Foundation4DateVSgvp" class="token"><code>earliestStartTime</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The earliest start time of incidents to be queried. If the value is null filtering by the earliest start time is not applied.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var earliestStartTime: Date?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk28TrafficIncidentsQueryOptionsV13latestEndTime10Foundation4DateVSgvp"></span>` `<span id="//apple_ref/swift/Property/latestEndTime" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-trafficincidentsqueryoptions#/s:7heresdk28TrafficIncidentsQueryOptionsV13latestEndTime10Foundation4DateVSgvp" class="token"><code>latestEndTime</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The latest end time of incidents to be queried. If the value is null filtering by the latest end time is not applied.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var latestEndTime: Date?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk28TrafficIncidentsQueryOptionsV12languageCodeAA08LanguageG0OSgvp"></span>` `<span id="//apple_ref/swift/Property/languageCode" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-trafficincidentsqueryoptions#/s:7heresdk28TrafficIncidentsQueryOptionsV12languageCodeAA08LanguageG0OSgvp" class="token"><code>languageCode</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The language code of the query. It’s the expected language of fields `description` and <a href="sdk-for-ios-navigate-classes-trafficincident#/s:7heresdk15TrafficIncidentC7summaryAA13LocalizedTextVvp">`TrafficIncident.summary`</a> in the relevant response. However, the language code doesn’t impact on <a href="sdk-for-ios-navigate-structs-trafficlocation#/s:7heresdk15TrafficLocationV11descriptionSSvp">`TrafficLocation.description`</a>. If the language code is null or not supported then response fields are expected in the original language of the country that the incident belongs to.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var languageCode: LanguageCode?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(typeFilter: impactFilter: earliestStartTime: latestEndTime: languageCode: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Undocumented

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( typeFilter : [ TrafficIncidentType ] = [], impactFilter : [ TrafficIncidentImpact ] = [], earliestStartTime : Date ? = nil , latestEndTime : Date ? = nil , languageCode : LanguageCode ? = nil )
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

