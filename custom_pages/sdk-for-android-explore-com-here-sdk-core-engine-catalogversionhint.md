---
title: "CatalogVersionHint (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-engine-catalogversionhint"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.core.engine](sdk-for-android-explore-com-here-sdk-core-engine-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
com.here.NativeBasecom.here.sdk.core.engine.CatalogVersionHint →
com.here.NativeBase → com.here.sdk.core.engine.CatalogVersionHint

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">CatalogVersionHint</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

This is a class for capturing user's intent for the desired catalog
version to use in DesiredCatalog class. You can request a specific or
latest version of a catalog by calling the static functions
specific(long) and latest(boolean) respectively. The HERE platform will
make the best effort to provide an appropriate version for the catalog
based on this version hint. Please take note that for the API
specific(long) to function properly, it is essential that the mutable
and persistent storage should be cleaned.

</div>

</div>

<div class="section summary">

- <div id="sdk-for-android-explore-method-summary"
  class="section method-summary">

  <div id="sdk-for-android-explore-method-summary-table">

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Method

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `[`CatalogVersionHint`](sdk-for-android-explore-com-here-sdk-core-engine-catalogversionhint "class in com.here.sdk.core.engine")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      latest(boolean ignoreCachedData)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  This static method can be called when you are interested in getting
  the most latest version of a catalog when initializing the HERE SDK
  with SDKOptions where you can specify the catalog(s) you want to use.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `[`CatalogVersionHint`](sdk-for-android-explore-com-here-sdk-core-engine-catalogversionhint "class in com.here.sdk.core.engine")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      specific(long version)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  This static method is used when you are interested in a specific
  version of a catalog, that you want to specify manually.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
  class="external-link" title="class or interface in java.lang">Object</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()"
  class="external-link"
  title="class or interface in java.lang"><code>clone</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)"
  class="external-link"
  title="class or interface in java.lang"><code>equals</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()"
  class="external-link"
  title="class or interface in java.lang"><code>hashCode</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()"
  class="external-link"
  title="class or interface in java.lang"><code>notify</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()"
  class="external-link"
  title="class or interface in java.lang"><code>notifyAll</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()"
  class="external-link"
  title="class or interface in java.lang"><code>toString</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

</div>

<div class="section details">

- <div id="sdk-for-android-explore-method-detail"
  class="section method-details">

  - <div id="sdk-for-android-explore-specific(long)"
    class="section detail">

    ### specific

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    static</span> <span class="return-type">[CatalogVersionHint](sdk-for-android-explore-com-here-sdk-core-engine-catalogversionhint "class in com.here.sdk.core.engine")</span> <span class="element-name">specific</span><span class="parameters">(long version)</span>

    </div>

    <div class="block">

    This static method is used when you are interested in a specific
    version of a catalog, that you want to specify manually. To ensure
    proper functioning of this API, it is essential to clean the mutable
    and persistent storage.

    </div>

    Parameters:  
    `version` -

    An integer value indicating the version of catalog desired. If the
    desired version does not exist, the HERE platform will make the best
    effort to provide an appropriate version or result in error logs
    about invalid version.

    Returns:  
    Instance of
    [`CatalogVersionHint`](sdk-for-android-explore-com-here-sdk-core-engine-catalogversionhint "class in com.here.sdk.core.engine")
    with specified version.

    </div>

  - <div id="sdk-for-android-explore-latest(boolean)"
    class="section detail">

    ### latest

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    static</span> <span class="return-type">[CatalogVersionHint](sdk-for-android-explore-com-here-sdk-core-engine-catalogversionhint "class in com.here.sdk.core.engine")</span> <span class="element-name">latest</span><span class="parameters">(boolean ignoreCachedData)</span>

    </div>

    <div class="block">

    This static method can be called when you are interested in getting
    the most latest version of a catalog when initializing the HERE SDK
    with SDKOptions where you can specify the catalog(s) you want to
    use. In effect, this will auto-update the cached map data on each
    start, if possible. Use this only when you have no installed Regions
    . Since this affects only the map data cache, calling this at
    initialization time has no or only a very limited effect on the
    start-up time. In order to auto-update cached OCM-based map data,
    such as for the HERE SDK (Navigate), use the default HRN value:
    "hrn:here:data::olp-here:ocm" in your DesiredCatalog . Note that the
    HERE SDK (Explore) cannot be used with such settings and the
    initialization of the HERE SDK may fail - since it is based on a
    different map format.

    </div>

    Parameters:  
    `ignoreCachedData` -

    A flag to specify handling of any cached data present on a device
    when trying to update the map version. If set to true, the HERE SDK
    will auto-update to the latest catalog version when no installed
    `Regions` are present. If present, this call will have no effect -
    use

        updateCatalog()

    via `MapUpdater` instead to update all map data to the latest
    version. Note that cached data present on a device - for example,
    data in the map cache or data cached by
    `PrefetchAroundLocationWithRadius` or
    `PrefetchAroundRouteOnIntervals` - will be become obsolete if a
    newer map version is available. Such data will be evicted using a
    LRU strategy over time. If set to false, the HERE SDK will
    auto-update to use the latest version, only when there is no cached
    map data at all (for example, at first install or after clearing the
    cache) *and* no installed map data. Otherwise, this call will have
    no effect.

    Returns:  
    Instance of
    [`CatalogVersionHint`](sdk-for-android-explore-com-here-sdk-core-engine-catalogversionhint "class in com.here.sdk.core.engine").

    </div>

  </div>

</div>

