---
title: "SDKOptions (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.core.engine](sdk-for-android-explore-com-here-sdk-core-engine-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.core.engine.SDKOptions

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">SDKOptions</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

SDKOptions provide an alternative way to set or update the HERE SDK
credentials and other parameters at runtime to initialize the
SDKNativeEngine .

</div>

</div>

<div class="section summary">

- <div id="nested-class-summary" class="section nested-class-summary">

  <div class="caption">

  Nested Classes

  </div>

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Class</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><code>static enum </code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions-actiononcachelock"
  class="type-name-link"
  title="enum class in com.here.sdk.core.engine"><code>SDKOptions.ActionOnCacheLock</code></a></td>
  <td><div class="block">
  Action on cache lock
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

- <div id="field-summary" class="section field-summary">

  <div class="caption">

  Fields

  </div>

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Field</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions-actiononcachelock"
  title="enum class in com.here.sdk.core.engine"><code>SDKOptions.ActionOnCacheLock</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#actionOnCacheLock"
  class="member-name-link"><code>actionOnCacheLock</code></a></td>
  <td><div class="block">
  Specifies action to perform when cache folder is locked by another
  process.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-authenticationmode"
  title="class in com.here.sdk.core.engine"><code>AuthenticationMode</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#authenticationMode"
  class="member-name-link"><code>authenticationMode</code></a></td>
  <td><div class="block">
  Encapsulates Authentication method and parameters.
  </div></td>
  </tr>
  <tr>
  <td><code>boolean</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#autoUpdateOfOnlineCache"
  class="member-name-link"><code>autoUpdateOfOnlineCache</code></a></td>
  <td><div class="block">
  Parameter to enable automatic cache updates.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#billingTag"
  class="member-name-link"><code>billingTag</code></a></td>
  <td><div class="block">
  Internal to HERE SDK.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#cachePath"
  class="member-name-link"><code>cachePath</code></a></td>
  <td><div class="block">
  Path to be used for caching purposes.
  </div></td>
  </tr>
  <tr>
  <td><code>long</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#cacheSizeInBytes"
  class="member-name-link"><code>cacheSizeInBytes</code></a></td>
  <td><div class="block">
  Desired upper bound of application size in bytes.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-catalogconfiguration"
  title="class in com.here.sdk.core.engine"><code>CatalogConfiguration</code></a><code>&gt;</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#catalogConfigurations"
  class="member-name-link"><code>catalogConfigurations</code></a></td>
  <td><div class="block">
  This field specifies how the SDKNativeEngine should access, use and
  store data for different catalogs.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
  class="external-link"
  title="class or interface in java.util"><code>Map</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-enginebaseurl"
  title="enum class in com.here.sdk.core.engine"><code>EngineBaseURL</code></a><code>,</code><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-engineoptions"
  title="class in com.here.sdk.core.engine"><code>EngineOptions</code></a><code>&gt;</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#customEngineOptions"
  class="member-name-link"><code>customEngineOptions</code></a></td>
  <td><div class="block">
  Set custom options for SDK Engines.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-metadata"
  title="class in com.here.sdk.core"><code>Metadata</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#customOptions"
  class="member-name-link"><code>customOptions</code></a></td>
  <td><div class="block">
  Options that define custom behavior for the HERE SDK.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#dataPath"
  class="member-name-link"><code>dataPath</code></a></td>
  <td><div class="block">
  Path used for storing application internal data, such as the offline
  search index and other essential data required for proper functionality.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration"
  title="class in com.here.sdk.core.engine"><code>LayerConfiguration</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#layerConfiguration"
  class="member-name-link"><code>layerConfiguration</code></a></td>
  <td><div class="block">
  Defines a list of data features that can be enabled / disabled.
  </div></td>
  </tr>
  <tr>
  <td><code>boolean</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#lowMemoryMode"
  class="member-name-link"><code>lowMemoryMode</code></a></td>
  <td><div class="block">
  If an application runs in a memory-constrained environment, enable this
  option to reduce the HERE SDK's memory footprint.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-networksettings"
  title="class in com.here.sdk.core.engine"><code>NetworkSettings</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#networkSettings"
  class="member-name-link"><code>networkSettings</code></a></td>
  <td><div class="block">
  Network settings to use at the start.
  </div></td>
  </tr>
  <tr>
  <td><code>boolean</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#offlineMode"
  class="member-name-link"><code>offlineMode</code></a></td>
  <td><div class="block">
  Sets offline mode for the HERE SDK.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#persistentMapStoragePath"
  class="member-name-link"><code>persistentMapStoragePath</code></a></td>
  <td><div class="block">
  Path to store persistent map data.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#politicalView"
  class="member-name-link"><code>politicalView</code></a></td>
  <td><div class="block">
  Geopolitical view of a country, defined as a three letter country code
  by ISO 3166-1 alpha-3.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#scope"
  class="member-name-link"><code>scope</code></a></td>
  <td><div class="block">
  Optional project ID to set the project scope of the login session.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

- <div id="constructor-summary" class="section constructor-summary">

  <div class="caption">

  Constructors

  </div>

  <table>
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <thead>
  <tr>
  <th>Constructor</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><pre><code>SDKOptions(AuthenticationMode authenticationMode)</code></pre></td>
  <td><div class="block">
  Constructs a SDKOptions from authentication mode.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

- <div id="method-summary" class="section method-summary">

  <div id="method-summary-table">

  <div class="table-tabs" aria-orientation="horizontal" role="tablist">

  All Methods
  Instance Methods
  Concrete Methods

  </div>

  <div id="method-summary-table.tabpanel"
  aria-labelledby="method-summary-table-tab0" role="tabpanel">

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Method</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><code>boolean</code></td>
  <td><pre><code>equals(Object obj)</code></pre></td>
  <td> </td>
  </tr>
  <tr>
  <td><code>int</code></td>
  <td><pre><code>hashCode()</code></pre></td>
  <td> </td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
  class="external-link" title="class or interface in java.lang">Object</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()"
  class="external-link"
  title="class or interface in java.lang"><code>clone</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()"
  class="external-link"
  title="class or interface in java.lang"><code>notify</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()"
  class="external-link"
  title="class or interface in java.lang"><code>notifyAll</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()"
  class="external-link"
  title="class or interface in java.lang"><code>toString</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

</div>

<div class="section details">

- <div id="field-detail" class="section field-details">

  - <div id="scope" class="section detail">

    ### scope

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">scope</span>

    </div>

    <div class="block">

    Optional project ID to set the project scope of the login session.
    Not used if empty. see also Manage Projects and IAM Concepts

    </div>

    </div>

  - <div id="cachePath" class="section detail">

    ### cachePath

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">cachePath</span>

    </div>

    <div class="block">

    Path to be used for caching purposes. It should be a path to the
    desired location where the application has read/write permissions.
    The path can be on internal or external storage. By default, this
    returns an empty string. Setting a new string, will overwrite the
    internally used default paths: Context.getCacheDir().getPath() . If
    an absolute path is set, it will be used instead. If a relative path
    is set then directory Context.getCacheDir().getPath() is used as
    parent path. Note, The cache path should be located under
    app-specific directory . Using shared directories such as Documents
    is not recommended as it will expose HERE SDK files to the other
    apps. It will also require additional permissions such as
    MANAGE_EXTERNAL_STORAGE and results in a poorer HERE SDK performance
    overall. The recommended location in terms of file I/O speed is the
    app's internal storage directory, whereas an external SD card is
    expected to be slower. This also depends on the quality of the used
    SD card.

    </div>

    </div>

  - <div id="cacheSizeInBytes" class="section detail">

    ### cacheSizeInBytes

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">cacheSizeInBytes</span>

    </div>

    <div class="block">

    Desired upper bound of application size in bytes. When cached data
    exceeds cache_size, least recently used data will be removed.
    Default value 256MB

    </div>

    </div>

  - <div id="dataPath" class="section detail">

    ### dataPath

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">dataPath</span>

    </div>

    <div class="block">

    Path used for storing application internal data, such as the offline
    search index and other essential data required for proper
    functionality. Note: For common use cases, prefer
    persistentMapStoragePath , or keep the default paths. Use dataPath
    only as a fallback if persistentMapStoragePath is not writable, for
    example, when you have an agreement with HERE to flash data at
    factory time. By default, this returns an empty string. In this
    case, the same path as persistentMapStoragePath will be used. If an
    absolute path is set, it will be used instead. If a relative path is
    set then directory Context.getFilesDir().getPath() is used as parent
    path. Application must have read/write permissions to the given
    desired path. It is recommended that the application has exclusive
    access to this path. Avoid using shared or public directories such
    as Download or Documents . Using such directories may cause certain
    HERE SDK features to behave with limitations. For example, index
    creation for offline search may fail or not function as expected. It
    is recommended not to use the application cache paths like
    Context.getCacheDir().getPath() , since operating system manages
    data in this location and data can be deleted if the device is low
    on storage space, which will result in application malfunction. The
    path can be on internal or external storage. The internal storage is
    recommended due to the file I/O speed. Note: If the
    persistentMapStoragePath is writable, dataPath can be left empty. If
    the persistentMapStoragePath is not writable, dataPath must be set
    and also be writable. Note that dataPath is used to store essential
    HERE SDK data. Important: There is no automatic migration of stored
    data between the persistentMapStoragePath and the dataPath . For
    ease of management, it's recommended to set the persistence path as
    writable and ignore dataPath . If dataPath is set differently from
    the persistentMapStoragePath , some data that would typically be
    saved in the persistentMapStoragePath will now be saved to dataPath
    . If dataPath is set and later unset, any data stored there will
    remain inaccessible and will not be migrated back.

    </div>

    </div>

  - <div id="persistentMapStoragePath" class="section detail">

    ### persistentMapStoragePath

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">persistentMapStoragePath</span>

    </div>

    <div class="block">

    Path to store persistent map data. This should be the a path to the
    desired location for which the application has read/write
    permissions. The path can be on internal or external storage. By
    default, this returns an empty string. Setting a new string, will
    overwrite the internally used default paths:
    Context.getFilesDir().getPath() . If an absolute path is set, it
    will be used instead. If a relative path is set then directory
    Context.getFilesDir().getPath() is used as parent path. Note :
    Offline maps stored at /v1/ /ocm-map/ , where is taken from
    SDKOptions.authenticationMode . When SDKOptions initialized with
    AuthenticationMode.withToken or AuthenticationMode.withExternal ,
    then left empty. Note, persistent map storage path should be located
    under app-specific directory . Using shared directories such as
    Documents is not recommended as it will expose HERE SDK files to the
    other apps. It will also require additional permissions such as
    MANAGE_EXTERNAL_STORAGE and results in a poorer HERE SDK performance
    overall. Additionally, the Android MediaProvider imposes certain
    restrictions on the creation of non-media files (such as temporary
    files or database files), which may cause some functionality to not
    behave as expected. The recommended location in terms of file I/O
    speed is the app's internal storage directory, whereas an external
    SD card is expected to be slower. This also depends on the quality
    of the used SD card. Note: If the persistent map storage location
    has the read only permission, then the dataPath must be configured.

    </div>

    </div>

  - <div id="politicalView" class="section detail">

    ### politicalView

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">politicalView</span>

    </div>

    <div class="block">

    Geopolitical view of a country, defined as a three letter country
    code by ISO 3166-1 alpha-3. Each disputed territory has an
    international and an alternative geopolitical view. When set, the
    map view will show all country boundaries according to the
    geopolitical view of the country that has been set. Note: Defaults
    to an empty string which enables the international view. This is a
    beta feature and thus there can be bugs and unexpected behavior.

    </div>

    </div>

  - <div id="offlineMode" class="section detail">

    ### offlineMode

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">offlineMode</span>

    </div>

    <div class="block">

    Sets offline mode for the HERE SDK. Defaults to false . When
    enabled, this prevents the HERE SDK from initiating any online
    connection from starting. The mode can be disabled or enabled again
    at any time via SDKNativeEngine.isOfflineMode() .

    </div>

    </div>

  - <div id="layerConfiguration" class="section detail">

    ### layerConfiguration

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[LayerConfiguration](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration "class in com.here.sdk.core.engine")</span> <span class="element-name">layerConfiguration</span>

    </div>

    <div class="block">

    Defines a list of data features that can be enabled / disabled. Once
    set to SDKOptions when a new HERE SDK is constructed, it will affect
    the map cache and offline maps. When disabling certain features,
    less data will be prefetched when the map is rendered. Map data that
    was already cached will not be removed until the least recently used
    strategy (LRU) applies. That means you cannot remove any content
    from the map cache by updating the LayerConfiguration . However, for
    new map data, it will be applied. For offline maps, this
    LayerConfiguration can reduce the download size of all regions. Note
    that the LayerConfiguration is applied globally to all regions that
    will be downloaded in the future. It will not affect already
    downloaded regions. Updating a region will also not update the
    LayerConfiguration . Only the LayerConfiguration will be used that
    was set globally when a region was downloaded for the first time. If
    you want to update the LayerConfiguration for an already downloaded
    region, please delete the region and download it again. Please also
    note The LayerConfiguration is only applicable for the HERE SDK
    (Navigate) that contains the offline maps feature. It has no effect
    on other licenses. The LayerConfiguration cannot be set separately
    for a region, it will be applied globally for all regions that will
    be downloaded in the future. It is not possible to specify a
    separate LayerConfiguration for the map cache and offline maps. The
    LayerConfiguration will be always applied to both. The
    LayerConfiguration does affect the map cache when a device has
    connectivity. Even when a device has connectivity it will only
    download the specified layers. This is a beta feature and thus there
    can be bugs and unexpected behavior.

    </div>

    </div>

  - <div id="catalogConfigurations" class="section detail">

    ### catalogConfigurations

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[CatalogConfiguration](sdk-for-android-explore-com-here-sdk-core-engine-catalogconfiguration "class in com.here.sdk.core.engine")></span> <span class="element-name">catalogConfigurations</span>

    </div>

    <div class="block">

    This field specifies how the SDKNativeEngine should access, use and
    store data for different catalogs. You can access default catalogs
    on the HERE platform and also custom catalogs such as for
    self-hosted or BYOD (bring your own data) use cases. For further
    information about catalogs and related concepts see
    CatalogConfiguration Note: This API is only available for the
    Navigate license. It has no affect on other license.

    </div>

    </div>

  - <div id="autoUpdateOfOnlineCache" class="section detail">

    ### autoUpdateOfOnlineCache

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">autoUpdateOfOnlineCache</span>

    </div>

    <div class="block">

    Parameter to enable automatic cache updates. When it is false, the
    cache will always use the same map version as offline maps. If
    offline maps are updated, the cache will be also updated. The cache
    version will never be older than the offline maps version. When it
    is true, the cache will be automatically updated to use the latest
    map data that is available. In that case, the cache may contain map
    data that is newer than the offline maps data. Note that auto
    updates may also lead to increased network traffic, as the cached
    data will be evicted tile-by-tile before it is filled with newer map
    data. This process continues everytime the user views a new map view
    area until the data is replaced. Once also the offline map data is
    updated by the user, both map versions will be the same again. If
    the value is also specified via the manifest (Android) or plist
    (iOS), than the value set via SDKOptions will overrule the value
    that was set in manifest/plist - until the current session ends and
    the value is read/set again. Note that offline maps are only
    available for the Navigate license. Defaults to false . Note: Do not
    use this yet, the behavior of this feature may be inconsistent. Once
    it will be usable, it will be announced in the regular HERE SDK
    release notes.

    </div>

    </div>

  - <div id="customEngineOptions" class="section detail">

    ### customEngineOptions

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
    class="external-link" title="class or interface in java.util">Map</a><[EngineBaseURL](sdk-for-android-explore-com-here-sdk-core-engine-enginebaseurl "enum class in com.here.sdk.core.engine"),[EngineOptions](sdk-for-android-explore-com-here-sdk-core-engine-engineoptions "class in com.here.sdk.core.engine")></span> <span class="element-name">customEngineOptions</span>

    </div>

    <div class="block">

    Set custom options for SDK Engines. This includes: custom_base_url :
    Allows engines to use custom base URLs for alternative services. By
    default, the available endpoints use HERE backend endpoints. If
    unsupported base URLs are specified, the related features will
    become non-functional. Please contact your HERE representative to
    learn about possible custom base URL usage options.
    custom_authentication_mode : Enables bearer authentication mode for
    engines, which adds or omits the header ("Authorization", "Bearer
    \$Token") to each online request made by the module the object is
    added to. The token (if used) can be provided directly or retrieved
    via key/secret from a dedicated backend. Note: This is a beta
    release of this feature, so there could be a few bugs and unexpected
    behaviors. Related APIs may change for new releases without a
    deprecation process.

    </div>

    </div>

  - <div id="actionOnCacheLock" class="section detail">

    ### actionOnCacheLock

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[SDKOptions.ActionOnCacheLock](sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions-actiononcachelock "enum class in com.here.sdk.core.engine")</span> <span class="element-name">actionOnCacheLock</span>

    </div>

    <div class="block">

    Specifies action to perform when cache folder is locked by another
    process. Default value is
    SDKOptions.ActionOnCacheLock.WAIT_LOCKING_APP_FINISH .

    </div>

    </div>

  - <div id="authenticationMode" class="section detail">

    ### authenticationMode

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[AuthenticationMode](sdk-for-android-explore-com-here-sdk-core-engine-authenticationmode "class in com.here.sdk.core.engine")</span> <span class="element-name">authenticationMode</span>

    </div>

    <div class="block">

    Encapsulates Authentication method and parameters.

    </div>

    </div>

  - <div id="networkSettings" class="section detail">

    ### networkSettings

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[NetworkSettings](sdk-for-android-explore-com-here-sdk-core-engine-networksettings "class in com.here.sdk.core.engine")</span> <span class="element-name">networkSettings</span>

    </div>

    <div class="block">

    Network settings to use at the start. Some of those settings can be
    changed later.

    </div>

    </div>

  - <div id="lowMemoryMode" class="section detail">

    ### lowMemoryMode

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">lowMemoryMode</span>

    </div>

    <div class="block">

    If an application runs in a memory-constrained environment, enable
    this option to reduce the HERE SDK's memory footprint. When set to
    true configures internal memory caches to consume less memory.
    Reduction in cache sizes also reduces performance of the HERE SDK.
    In order to release memory occupied by internal caches see
    SDKNativeEngine.purgeMemoryCaches(com.here.sdk.core.engine.SDKNativeEngine.PurgeMemoryStrategy)
    .

    </div>

    </div>

  - <div id="billingTag" class="section detail">

    ### billingTag

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">billingTag</span>

    </div>

    <div class="block">

    Internal to HERE SDK. DO NOT USE THIS YET. Warning: This is a
    placeholder and under developement. We will announce its
    availability in our changelog once it is ready for use. A parameter
    to set a billing tag to track your HERE platform usage across the
    various HERE services your application may contact. For more
    information on the billing tag, see our cost management guide . The
    tag needs to follow the format as described in the guide or it will
    be ignored. The parameter defaults to null , which also means that
    the tag is ignored for all requests. Note: The billing tag is
    optional, but when set, it can help you to understand how often your
    app uses certain services, for example, the number of hits to our
    HERE backend routing services. For more details on tracking such
    details, please consult the cost management guide or get in touch
    with the HERE billing team.

    </div>

    </div>

  - <div id="customOptions" class="section detail">

    ### customOptions

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[Metadata](sdk-for-android-explore-com-here-sdk-core-metadata "class in com.here.sdk.core")</span> <span class="element-name">customOptions</span>

    </div>

    <div class="block">

    Options that define custom behavior for the HERE SDK. These settings
    allow fine-tuning of internal thread pools and resource management
    for advanced use cases. These options are intended for internal
    usage only and should not be modified unless instructed by HERE
    support. Note: This is a beta release of this feature, so there
    could be a few bugs and unexpected behaviors. Related APIs may
    change for new releases without a deprecation process.

    </div>

    </div>

  </div>

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>(com.here.sdk.core.engine.AuthenticationMode)"
    class="section detail">

    ### SDKOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">SDKOptions</span><span class="parameters">(@NonNull
    [AuthenticationMode](sdk-for-android-explore-com-here-sdk-core-engine-authenticationmode "class in com.here.sdk.core.engine") authenticationMode)</span>

    </div>

    <div class="block">

    Constructs a SDKOptions from authentication mode. Other fields are
    filled with default values.

    </div>

    Parameters:  
    `authenticationMode` -

    Authentication Mode used for obtaining an access token.

    </div>

  </div>

- <div id="method-detail" class="section method-details">

  - <div id="equals(java.lang.Object)" class="section detail">

    ### equals

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><span class="parameters">(<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
    class="external-link" title="class or interface in java.lang">Object</a> obj)</span>

    </div>

    Overrides:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)"
    class="external-link"
    title="class or interface in java.lang"><code>equals</code></a> in
    class <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
    class="external-link"
    title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="hashCode()" class="section detail">

    ### hashCode

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()

    </div>

    Overrides:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()"
    class="external-link"
    title="class or interface in java.lang"><code>hashCode</code></a> in
    class <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
    class="external-link"
    title="class or interface in java.lang"><code>Object</code></a>

    </div>

  </div>

</div>

