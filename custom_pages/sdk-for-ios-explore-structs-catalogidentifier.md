---
title: "CatalogIdentifier Structure Reference"
slug: "sdk-for-ios-explore-structs-catalogidentifier"
---

# CatalogIdentifier

<div class="declaration">

<div class="language">

``` highlight
public struct CatalogIdentifier : Hashable
```

</div>

</div>

This class is used to identify any catalog in the HERE platform.

A catalog is a storage-representation to store map data on the HERE platform. The data inside a catalog is divided into layers, where each layer consists of datasets with similar functional attributes in the physical world. For example, there can be a layer for road-topology, a layer for road-attributes (such as speed limits) and a layer for places and business addresses. All these layers, in different geographic regions, can be grouped together into a catalog to create a representation of the world we live in, called HERE map. It can be also used to render a <a href="sdk-for-ios-explore-classes-mapview">`MapView`</a>. Each geographic region is cut into geospatial tiles for efficient search, map display, routing, map matching, and driver warnings. Each tile partitions the map data (in one or more layers, depending on the product) in the geolocation of that specific tile. The data inside a catalog is logically managed and access controlled as a single set. If you have any data that you want to bring to the HERE platform, you need a catalog to contain it. For additional information about catalogs, and related concepts of data representation on the HERE platform, refer to <a href="https://www.here.com/docs/bundle/data-api-developer-guide/page/rest/catalogs.html">the Data API</a> and <a href="https://www.here.com/docs/bundle/introduction-to-mapping-concepts-user-guide/page/topics/maps-layers-tiles.html">Introduction to Mapping Concepts</a>

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17CatalogIdentifierV3hrnSSvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-hrn" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-catalogidentifier#sdk-for-ios-explore-s-7heresdk17CatalogIdentifierV3hrnSSvp" class="token"><code>hrn</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A HERE Resource Name (HRN) for this catalog. This is a unique string returned by the HERE platform when you add a new catalog to your project. For information about catalog creation process refer to <a href="https://www.here.com/docs/bundle/data-api-developer-guide/page/rest/creating-a-catalog.html">the Data API</a> By default, this field points to a default catalog on HERE platform, which contains data for the whole world excluding the region of Japan. Use <a href="sdk-for-ios-explore-structs-catalogconfiguration#sdk-for-ios-explore-s-7heresdk20CatalogConfigurationV10getDefault11catalogTypeAcA0bG0O_tFZ">`CatalogConfiguration.getDefault(...)`</a> to get the default HRN value for use with the HERE platform.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var hrn: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17CatalogIdentifierV7versions5Int64VSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-version" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-catalogidentifier#sdk-for-ios-explore-s-7heresdk17CatalogIdentifierV7versions5Int64VSgvp" class="token"><code>version</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A version number for a catalog. When accessing a catalog, this version must be specified. Set `nil` to automatically get the latest version for a catalog. The field defaults to `nil`. Since the data inside a catalog can be updated, each published modification needs to correlate to a specific version number. Note: when `CatalogIdentifier` created with <a href="sdk-for-ios-explore-structs-desiredcatalog">`DesiredCatalog`</a> then:

  - numerical `-1` corresponds to <a href="sdk-for-ios-explore-classes-catalogversionhint#sdk-for-ios-explore-s-7heresdk18CatalogVersionHintC6latest16ignoreCachedDataACSb_tFZ">`CatalogVersionHint.latest(...)`</a> with `ignoreCachedData` set to `true`;
  - `nil` corresponds to <a href="sdk-for-ios-explore-classes-catalogversionhint#sdk-for-ios-explore-s-7heresdk18CatalogVersionHintC6latest16ignoreCachedDataACSb_tFZ">`CatalogVersionHint.latest(...)`</a> with `ignoreCachedData` set to `false`;
  - other numerical values correspond to `version` passed to <a href="sdk-for-ios-explore-classes-catalogversionhint#sdk-for-ios-explore-s-7heresdk18CatalogVersionHintC8specific7versionACs5Int64V_tFZ">`CatalogVersionHint.specific(...)`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var version: Int64?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17CatalogIdentifierV3hrn7versionACSS_s5Int64VSgtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-hrn-version" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-catalogidentifier#sdk-for-ios-explore-s-7heresdk17CatalogIdentifierV3hrn7versionACSS_s5Int64VSgtcfc" class="token"><code>init(hrn:</code><wbr></wbr><code>version:</code><wbr></wbr><code>)</code></a> 

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
  public init(hrn: String = "hrn:here:data::olp-here:ocm", version: Int64? = nil)
  ```

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

