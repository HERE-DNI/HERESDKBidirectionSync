---
title: "CatalogVersionHint Class Reference"
slug: "sdk-for-ios-explore-classes-catalogversionhint"
---

# CatalogVersionHint

<div class="declaration">

<div class="language">

``` highlight
public class CatalogVersionHint
```

``` highlight
extension CatalogVersionHint: NativeBase
```

``` highlight
extension CatalogVersionHint: Hashable
```

</div>

</div>

This is a class for capturing user’s intent for the desired catalog version to use in <a href="sdk-for-ios-explore-structs-desiredcatalog">`DesiredCatalog`</a> class.

You can request a specific or latest version of a catalog by calling the static functions

    CatalogVersionHint.specific(...)

and

    CatalogVersionHint.latest(...)

respectively. The HERE platform will make the best effort to provide an appropriate version for the catalog based on this version hint. Please take note that for the API

    CatalogVersionHint.specific(...)

to function properly, it is essential that the mutable and persistent storage should be cleaned.
</p>

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

      specific(version: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This static method is used when you are interested in a specific version of a catalog, that you want to specify manually. To ensure proper functioning of this API, it is essential to clean the mutable and persistent storage.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func specific ( version : Int64 ) -> CatalogVersionHint
  ```

  </pre>

  </div>

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
  <td><code> </code><em><code>version</code></em><code> </code></td>
  <td><div>
  <p>An integer value indicating the version of catalog desired. If the desired version does not exist, the HERE platform will make the best effort to provide an appropriate version or result in error logs about invalid version.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Instance of `CatalogVersionHint` with specified version.

  </div>

  </div>

  </div>

- <div>

      latest(ignoreCachedData: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This static method can be called when you are interested in getting the most latest version of a catalog when initializing the HERE SDK with <a href="sdk-for-ios-explore-structs-sdkoptions">`SDKOptions`</a> where you can specify the catalog(s) you want to use. In effect, this will auto-update the cached map data on each start, if possible. Use this only when you have no installed `Regions`. Since this affects only the map data cache, calling this at initialization time has no or only a very limited effect on the start-up time.

  In order to auto-update cached OCM-based map data, such as for the HERE SDK (Navigate), use the default HRN value: “hrn:here:data::olp-here:ocm” in your <a href="sdk-for-ios-explore-structs-desiredcatalog">`DesiredCatalog`</a>. Note that the HERE SDK (Explore) cannot be used with such settings and the initialization of the HERE SDK may fail - since it is based on a different map format.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func latest ( ignoreCachedData : Bool ) -> CatalogVersionHint
  ```

  </pre>

  </div>

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
  <td><code> </code><em><code>ignoreCachedData</code></em><code> </code></td>
  <td><div>
  <p>A flag to specify handling of any cached data present on a device when trying to update the map version. If set to true, the HERE SDK will auto-update to the latest catalog version when no installed <code>Regions</code> are present. If present, this call will have no effect - use</p>
  <pre><code>updateCatalog()</code></pre>
  via <a href="sdk-for-ios-explore-classes-mapupdater"><code>MapUpdater</code></a> instead to update all map data to the latest version. Note that cached data present on a device - for example, data in the map cache or data cached by <code>PrefetchAroundLocationWithRadius</code> or <code>PrefetchAroundRouteOnIntervals</code> - will be become obsolete if a newer map version is available. Such data will be evicted using a LRU strategy over time. If set to false, the HERE SDK will auto-update to use the latest version, only when there is no cached map data at all (for example, at first install or after clearing the cache) <em>and</em> no installed map data. Otherwise, this call will have no effect.
  </p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Instance of `CatalogVersionHint`.

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

