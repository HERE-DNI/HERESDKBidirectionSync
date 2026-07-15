---
title: "Ev Structure Reference"
slug: "sdk-for-ios-explore-structs-placefilter-ev"
---

# Ev

<div class="declaration">

<div class="language">

``` highlight
public struct Ev : Hashable
```

</div>

</div>

Constraints that are applicable on the places of category EV station.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk11PlaceFilterV2EvV13supplierNamesSaySSGvp"></span>` `<span id="//apple_ref/swift/Property/supplierNames" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-placefilter-ev#/s:7heresdk11PlaceFilterV2EvV13supplierNamesSaySSGvp" class="token"><code>supplierNames</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets a constraint on the charge point operator name of the EV station.

  Not supported in <a href="sdk-for-ios-explore-classes-offlinesearchengine">`OfflineSearchEngine`</a> (only available for the Navigate license).

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var supplierNames: [String]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11PlaceFilterV2EvV16connectorTypeIDsSaySSGvp"></span>` `<span id="//apple_ref/swift/Property/connectorTypeIDs" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-placefilter-ev#/s:7heresdk11PlaceFilterV2EvV16connectorTypeIDsSaySSGvp" class="token"><code>connectorTypeIDs</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Filter to retrieve EV charging stations with at least one of the connector type IDs. For more information on the current connector types, see <https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-type-connector.html>

  Not supported in <a href="sdk-for-ios-explore-classes-offlinesearchengine">`OfflineSearchEngine`</a> (only available for the Navigate license).

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var connectorTypeIDs: [String]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11PlaceFilterV2EvV19minPowerInKilowattsSdSgvp"></span>` `<span id="//apple_ref/swift/Property/minPowerInKilowatts" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-placefilter-ev#/s:7heresdk11PlaceFilterV2EvV19minPowerInKilowattsSdSgvp" class="token"><code>minPowerInKilowatts</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Filter to retrieve EV charging stations with the given minimum charging power in KW delivered by at least one of the station EVSE. Not supported for `suggestByText` in <a href="sdk-for-ios-explore-classes-offlinesearchengine">`OfflineSearchEngine`</a> (only available for the Navigate license).

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var minPowerInKilowatts: Double?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11PlaceFilterV2EvV34eMobilityServiceProviderPartnerIDsSaySSGvp"></span>` `<span id="//apple_ref/swift/Property/eMobilityServiceProviderPartnerIDs" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-placefilter-ev#/s:7heresdk11PlaceFilterV2EvV34eMobilityServiceProviderPartnerIDsSaySSGvp" class="token"><code>eMobilityServiceProviderPartnerIDs</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Filter to retrieve EV charging stations with at least one matching e-Mobility Service Provider Partner ID.

  Not supported in <a href="sdk-for-ios-explore-classes-offlinesearchengine">`OfflineSearchEngine`</a> (only available for the Navigate license).

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var eMobilityServiceProviderPartnerIDs: [String]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11PlaceFilterV2EvV11currentTypeAA07CurrentF0OSgvp"></span>` `<span id="//apple_ref/swift/Property/currentType" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-placefilter-ev#/s:7heresdk11PlaceFilterV2EvV11currentTypeAA07CurrentF0OSgvp" class="token"><code>currentType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Filter to retrieve EV charging stations with the given current type provided at one of the station EVSE. Accepted is either AC or DC. Not supported for `suggestByText` in <a href="sdk-for-ios-explore-classes-offlinesearchengine">`OfflineSearchEngine`</a> (only available for the Navigate license).

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var currentType: CurrentType?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(supplierNames: connectorTypeIDs: minPowerInKilowatts: eMobilityServiceProviderPartnerIDs: currentType: )

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

    - supplierNames: Sets a constraint on the charge point operator name of the EV station.

    Not supported in <a href="sdk-for-ios-explore-classes-offlinesearchengine">`OfflineSearchEngine`</a> (only available for the Navigate license).

    - connectorTypeIDs: Filter to retrieve EV charging stations with at least one of the connector type IDs. For more information on the current connector types, see <https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-type-connector.html>

    Not supported in <a href="sdk-for-ios-explore-classes-offlinesearchengine">`OfflineSearchEngine`</a> (only available for the Navigate license).

    - minPowerInKilowatts: Filter to retrieve EV charging stations with the given minimum charging power in KW delivered by at least one of the station EVSE. Not supported for `suggestByText` in <a href="sdk-for-ios-explore-classes-offlinesearchengine">`OfflineSearchEngine`</a> (only available for the Navigate license).
    - eMobilityServiceProviderPartnerIDs: Filter to retrieve EV charging stations with at least one matching e-Mobility Service Provider Partner ID.

    Not supported in <a href="sdk-for-ios-explore-classes-offlinesearchengine">`OfflineSearchEngine`</a> (only available for the Navigate license).

    - currentType: Filter to retrieve EV charging stations with the given current type provided at one of the station EVSE. Accepted is either AC or DC. Not supported for `suggestByText` in <a href="sdk-for-ios-explore-classes-offlinesearchengine">`OfflineSearchEngine`</a> (only available for the Navigate license).

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( supplierNames : [ String ] = [], connectorTypeIDs : [ String ] = [], minPowerInKilowatts : Double ? = nil , eMobilityServiceProviderPartnerIDs : [ String ] = [], currentType : CurrentType ? = nil )
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

