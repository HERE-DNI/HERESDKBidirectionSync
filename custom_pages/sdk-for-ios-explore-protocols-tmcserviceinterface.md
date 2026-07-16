---
title: "TMCServiceInterface Protocol Reference"
slug: "sdk-for-ios-explore-protocols-tmcserviceinterface"
---

# TMCServiceInterface

<div class="declaration">

<div class="language">

``` highlight
public protocol TMCServiceInterface : AnyObject
```

</div>

</div>

Contains all outgoing dependencies to the client side.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19TMCServiceInterfaceP07requestB017tmcServiceRequestyAA0bG0V_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-requestTMCService-tmcServiceRequest" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-tmcserviceinterface#sdk-for-ios-explore-s-7heresdk19TMCServiceInterfaceP07requestB017tmcServiceRequestyAA0bG0V_tF" class="token"><code>requestTMCService(tmcServiceRequest:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Called whenever the traffic broadcast needs to be activated.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func requestTMCService(tmcServiceRequest: TMCServiceRequest)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-tmcservicerequest">TMCServiceRequest</a>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>tmcServiceRequest</code></em><code> </code></td>
  <td><div>
  <p>Parameters used to request the traffic broadcast.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19TMCServiceInterfaceP19getTMCPreferredSids012tmcPreferredF7RequestSays5UInt8VGAA0efI0V_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-getTMCPreferredSids-tmcPreferredSidsRequest" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-tmcserviceinterface#sdk-for-ios-explore-s-7heresdk19TMCServiceInterfaceP19getTMCPreferredSids012tmcPreferredF7RequestSays5UInt8VGAA0efI0V_tF" class="token"><code>getTMCPreferredSids(tmcPreferredSidsRequest:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Called whenever there is a need to get a list of preferred SIDs for a specific area.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func getTMCPreferredSids(tmcPreferredSidsRequest: TMCPreferredSidsRequest) -> [UInt8]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-tmcpreferredsidsrequest">TMCPreferredSidsRequest</a>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>tmcPreferredSidsRequest</code></em><code> </code></td>
  <td><div>
  <p>Specifies the area to request the preferred SIDs.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  List of preferred SIDs.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19TMCServiceInterfaceP20getRDSEncryptionKeys013rdsEncryptionF7RequestSayAA0E3KeyVGAA0efI0V_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-getRDSEncryptionKeys-rdsEncryptionKeysRequest" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-tmcserviceinterface#sdk-for-ios-explore-s-7heresdk19TMCServiceInterfaceP20getRDSEncryptionKeys013rdsEncryptionF7RequestSayAA0E3KeyVGAA0efI0V_tF" class="token"><code>getRDSEncryptionKeys(rdsEncryptionKeysRequest:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Called whenever there is a need to get RDS encryption keys.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func getRDSEncryptionKeys(rdsEncryptionKeysRequest: RDSEncryptionKeysRequest) -> [RDSEncryptionKey]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-rdsencryptionkeysrequest">RDSEncryptionKeysRequest</a>
  - <a href="sdk-for-ios-explore-structs-rdsencryptionkey">RDSEncryptionKey</a>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>rdsEncryptionKeysRequest</code></em><code> </code></td>
  <td><div>
  <p>Input data to search for keys.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  RDS encryption keys.

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

