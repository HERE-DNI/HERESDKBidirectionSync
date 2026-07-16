---
title: "VenueErrorCode Enumeration Reference"
slug: "sdk-for-ios-navigate-enums-venueerrorcode"
---

# VenueErrorCode

<div class="declaration">

<div class="language">

``` highlight
public enum VenueErrorCode : UInt32, CaseIterable, Codable
```

``` highlight
extension VenueErrorCode : Error
```

</div>

</div>

Specifies possible errors that may occur during loading of indoor maps

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14VenueErrorCodeO9noNetworkyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-noNetwork" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-venueerrorcode#sdk-for-ios-navigate-s-7heresdk14VenueErrorCodeO9noNetworkyA2CmF" class="token"><code>noNetwork</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  No network

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case noNetwork = 1
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14VenueErrorCodeO15noMetaDataFoundyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-noMetaDataFound" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-venueerrorcode#sdk-for-ios-navigate-s-7heresdk14VenueErrorCodeO15noMetaDataFoundyA2CmF" class="token"><code>noMetaDataFound</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Meta data missing error.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case noMetaDataFound
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14VenueErrorCodeO10hrnMissingyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-hrnMissing" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-venueerrorcode#sdk-for-ios-navigate-s-7heresdk14VenueErrorCodeO10hrnMissingyA2CmF" class="token"><code>hrnMissing</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  HRN not provided

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case hrnMissing
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14VenueErrorCodeO11hrnMismatchyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-hrnMismatch" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-venueerrorcode#sdk-for-ios-navigate-s-7heresdk14VenueErrorCodeO11hrnMismatchyA2CmF" class="token"><code>hrnMismatch</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  HRN missmatch.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case hrnMismatch
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14VenueErrorCodeO19noDefaultCollectionyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-noDefaultCollection" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-venueerrorcode#sdk-for-ios-navigate-s-7heresdk14VenueErrorCodeO19noDefaultCollectionyA2CmF" class="token"><code>noDefaultCollection</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Default collection missing.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case noDefaultCollection
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14VenueErrorCodeO13mapIdNotFoundyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-mapIdNotFound" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-venueerrorcode#sdk-for-ios-navigate-s-7heresdk14VenueErrorCodeO13mapIdNotFoundyA2CmF" class="token"><code>mapIdNotFound</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Map ID not found.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case mapIdNotFound
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14VenueErrorCodeO16mapDataIncorrectyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-mapDataIncorrect" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-venueerrorcode#sdk-for-ios-navigate-s-7heresdk14VenueErrorCodeO16mapDataIncorrectyA2CmF" class="token"><code>mapDataIncorrect</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Map data incorrect

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case mapDataIncorrect
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14VenueErrorCodeO17noMapInCollectionyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-noMapInCollection" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-venueerrorcode#sdk-for-ios-navigate-s-7heresdk14VenueErrorCodeO17noMapInCollectionyA2CmF" class="token"><code>noMapInCollection</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  No map available in collection

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case noMapInCollection
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14VenueErrorCodeO10badRequestyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-badRequest" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-venueerrorcode#sdk-for-ios-navigate-s-7heresdk14VenueErrorCodeO10badRequestyA2CmF" class="token"><code>badRequest</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Bad request.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case badRequest = 400
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14VenueErrorCodeO12tokenInvalidyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-tokenInvalid" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-venueerrorcode#sdk-for-ios-navigate-s-7heresdk14VenueErrorCodeO12tokenInvalidyA2CmF" class="token"><code>tokenInvalid</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Invalid authentication token

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case tokenInvalid = 401
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14VenueErrorCodeO8notFoundyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-notFound" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-venueerrorcode#sdk-for-ios-navigate-s-7heresdk14VenueErrorCodeO8notFoundyA2CmF" class="token"><code>notFound</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Requested resource not found.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case notFound = 404
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14VenueErrorCodeO014internalServerC0yA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-internalServerError" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-venueerrorcode#sdk-for-ios-navigate-s-7heresdk14VenueErrorCodeO014internalServerC0yA2CmF" class="token"><code>internalServerError</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Internal Server error

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case internalServerError = 500
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14VenueErrorCodeO18serviceUnavailableyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-serviceUnavailable" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-venueerrorcode#sdk-for-ios-navigate-s-7heresdk14VenueErrorCodeO18serviceUnavailableyA2CmF" class="token"><code>serviceUnavailable</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Service unavailable

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case serviceUnavailable = 502
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14VenueErrorCodeO15payloadTooLargeyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-payloadTooLarge" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-venueerrorcode#sdk-for-ios-navigate-s-7heresdk14VenueErrorCodeO15payloadTooLargeyA2CmF" class="token"><code>payloadTooLarge</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Payload too large.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case payloadTooLarge = 513
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

