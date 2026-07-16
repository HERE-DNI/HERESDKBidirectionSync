---
title: "TrafficRadio  Reference"
slug: "sdk-for-ios-navigate-trafficradio"
---

# TrafficRadio

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk16TrafficBroadcastC"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Class-TrafficBroadcast" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-trafficradio#sdk-for-ios-navigate-s-7heresdk16TrafficBroadcastC" class="token"><code>TrafficBroadcast</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A `TrafficBroadcast` is expecting the <a href="https://en.wikipedia.org/wiki/Traffic_message_channel">RDS-TMC</a> format and it can be used when there is no internet connection, so that the <a href="sdk-for-ios-navigate-classes-offlineroutingengine">`OfflineRoutingEngine`</a> can utilize traffic data coming over a radio channel. The <a href="sdk-for-ios-navigate-classes-trafficbroadcast#sdk-for-ios-navigate-s-7heresdk16TrafficBroadcastC8activateyyF">`TrafficBroadcast.activate(...)`</a> method needs to be called to receive traffic data events.

  **Note:** In order to adopt the <a href="sdk-for-ios-navigate-traffic#sdk-for-ios-navigate-s-7heresdk19TrafficDataProviderC">`TrafficDataProvider`</a> interface special hardware is required. Talk to your HERE representative for more details. Only by adopting the <a href="sdk-for-ios-navigate-traffic#sdk-for-ios-navigate-s-7heresdk19TrafficDataProviderC">`TrafficDataProvider`</a> interface you can integrate radio station signals providing traffic broadcasts. Traffic broadcasts are meant to be used *independently* from the already included traffic on routes, on the map and from the HERE backends (when using the <a href="sdk-for-ios-navigate-classes-trafficengine">`TrafficEngine`</a>).

  This class continuously reacts to new locations provided from a location source and acts as a <a href="sdk-for-ios-navigate-protocols-locationdelegate">`LocationDelegate`</a>. The location must be updated regardless of calling <a href="sdk-for-ios-navigate-classes-trafficbroadcast#sdk-for-ios-navigate-s-7heresdk16TrafficBroadcastC8activateyyF">`TrafficBroadcast.activate(...)`</a>.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-classes-trafficbroadcast" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class TrafficBroadcast : LocationDelegate
  ```

  ``` highlight
  extension TrafficBroadcast: NativeBase
  ```

  ``` highlight
  extension TrafficBroadcast: Hashable
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-protocols-locationdelegate">LocationDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk26TrafficBroadcastParametersV"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Struct-TrafficBroadcastParameters" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-trafficradio#sdk-for-ios-navigate-s-7heresdk26TrafficBroadcastParametersV" class="token"><code>TrafficBroadcastParameters</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the parameters needed to request the traffic broadcast.

  <a href="sdk-for-ios-navigate-structs-trafficbroadcastparameters" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct TrafficBroadcastParameters
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7TMCDataV"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Struct-TMCData" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-trafficradio#sdk-for-ios-navigate-s-7heresdk7TMCDataV" class="token"><code>TMCData</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the traffic events in RDS-TMC format.

  <a href="sdk-for-ios-navigate-structs-tmcdata" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct TMCData
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk23TMCPreferredSidsRequestV"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Struct-TMCPreferredSidsRequest" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-trafficradio#sdk-for-ios-navigate-s-7heresdk23TMCPreferredSidsRequestV" class="token"><code>TMCPreferredSidsRequest</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents data used to request the list of preferred SIDs.

  <a href="sdk-for-ios-navigate-structs-tmcpreferredsidsrequest" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct TMCPreferredSidsRequest
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22TMCServiceProviderInfoV"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Struct-TMCServiceProviderInfo" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-trafficradio#sdk-for-ios-navigate-s-7heresdk22TMCServiceProviderInfoV" class="token"><code>TMCServiceProviderInfo</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the service prodiver info in RDS-TMC format.

  <a href="sdk-for-ios-navigate-structs-tmcserviceproviderinfo" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct TMCServiceProviderInfo
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk17TMCServiceRequestV"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Struct-TMCServiceRequest" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-trafficradio#sdk-for-ios-navigate-s-7heresdk17TMCServiceRequestV" class="token"><code>TMCServiceRequest</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the parameters used to request the traffic broadcast.

  <a href="sdk-for-ios-navigate-structs-tmcservicerequest" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct TMCServiceRequest
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk19TMCServiceInterfaceP"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Protocol-TMCServiceInterface" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-trafficradio#sdk-for-ios-navigate-s-7heresdk19TMCServiceInterfaceP" class="token"><code>TMCServiceInterface</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Contains all outgoing dependencies to the client side.

  <a href="sdk-for-ios-navigate-protocols-tmcserviceinterface" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol TMCServiceInterface : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk16RDSEncryptionKeyV"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Struct-RDSEncryptionKey" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-trafficradio#sdk-for-ios-navigate-s-7heresdk16RDSEncryptionKeyV" class="token"><code>RDSEncryptionKey</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the RDS encryption key. Fields allocation information is described in CEN ISO/CD 14819-6.

  <a href="sdk-for-ios-navigate-structs-rdsencryptionkey" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct RDSEncryptionKey
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk24RDSEncryptionKeysRequestV"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Struct-RDSEncryptionKeysRequest" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-trafficradio#sdk-for-ios-navigate-s-7heresdk24RDSEncryptionKeysRequestV" class="token"><code>RDSEncryptionKeysRequest</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents data to search for RDS encryption keys.

  <a href="sdk-for-ios-navigate-structs-rdsencryptionkeysrequest" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct RDSEncryptionKeysRequest : Hashable
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

