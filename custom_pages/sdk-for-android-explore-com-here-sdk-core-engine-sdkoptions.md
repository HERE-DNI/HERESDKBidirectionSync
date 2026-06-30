---
title: "SDKOptions (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- SDKOptions.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.core.engine.SDKOptions</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">SDKOptions</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>SDKOptions provide an alternative way to set or update the HERE SDK credentials and other
 parameters at runtime to initialize the <a href="sdk-for-android-explore-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a>.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">

<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static enum </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions.actiononcachelock" title="enum class in com.here.sdk.core.engine">SDKOptions.ActionOnCacheLock</a></code></div>
<div class="col-last even-row-color">
<div class="block">Action on cache lock</div>
</div>
</div>
</section>
</li>
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">

<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions.actiononcachelock" title="enum class in com.here.sdk.core.engine">SDKOptions.ActionOnCacheLock</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#actionOnCacheLock">actionOnCacheLock</a></code></div>
<div class="col-last even-row-color">
<div class="block">Specifies action to perform when cache folder is locked by another process.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-explore-com-here-sdk-core-engine-authenticationmode" title="class in com.here.sdk.core.engine">AuthenticationMode</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#authenticationMode">authenticationMode</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Encapsulates Authentication method and parameters.</div>
</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#autoUpdateOfOnlineCache">autoUpdateOfOnlineCache</a></code></div>
<div class="col-last even-row-color">
<div class="block">Parameter to enable automatic cache updates.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#billingTag">billingTag</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Internal to HERE SDK.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#cachePath">cachePath</a></code></div>
<div class="col-last even-row-color">
<div class="block">Path to be used for caching purposes.</div>
</div>
<div class="col-first odd-row-color"><code>long</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#cacheSizeInBytes">cacheSizeInBytes</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Desired upper bound of application size in bytes.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-com-here-sdk-core-engine-catalogconfiguration" title="class in com.here.sdk.core.engine">CatalogConfiguration</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#catalogConfigurations">catalogConfigurations</a></code></div>
<div class="col-last even-row-color">
<div class="block">This field specifies how the <a href="sdk-for-android-explore-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a> should access, use and store
 data for different catalogs.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="sdk-for-android-explore-com-here-sdk-core-engine-enginebaseurl" title="enum class in com.here.sdk.core.engine">EngineBaseURL</a>,<wbr/><a href="sdk-for-android-explore-com-here-sdk-core-engine-engineoptions" title="class in com.here.sdk.core.engine">EngineOptions</a>&gt;</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#customEngineOptions">customEngineOptions</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Set custom options for SDK Engines.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-explore-com-here-sdk-core-metadata" title="class in com.here.sdk.core">Metadata</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#customOptions">customOptions</a></code></div>
<div class="col-last even-row-color">
<div class="block">Options that define custom behavior for the HERE SDK.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#dataPath">dataPath</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Path used for storing application internal data, such as the offline search index and other essential data required for proper functionality.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration" title="class in com.here.sdk.core.engine">LayerConfiguration</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#layerConfiguration">layerConfiguration</a></code></div>
<div class="col-last even-row-color">
<div class="block">Defines a list of data features that can be enabled / disabled.</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#lowMemoryMode">lowMemoryMode</a></code></div>
<div class="col-last odd-row-color">
<div class="block">If an application runs in a memory-constrained environment, enable this option to reduce the HERE SDK's memory footprint.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-explore-com-here-sdk-core-engine-networksettings" title="class in com.here.sdk.core.engine">NetworkSettings</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#networkSettings">networkSettings</a></code></div>
<div class="col-last even-row-color">
<div class="block">Network settings to use at the start.</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#offlineMode">offlineMode</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Sets offline mode for the HERE SDK.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#persistentMapStoragePath">persistentMapStoragePath</a></code></div>
<div class="col-last even-row-color">
<div class="block">Path to store persistent map data.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#politicalView">politicalView</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Geopolitical view of a country, defined as a three letter country code by ISO 3166-1 alpha-3.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#scope">scope</a></code></div>
<div class="col-last even-row-color">
<div class="block">Optional project ID to set the project scope of the login session.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#%3Cinit%3E(com.here.sdk.core.engine.AuthenticationMode)">SDKOptions</a><wbr/>(<a href="sdk-for-android-explore-com-here-sdk-core-engine-authenticationmode" title="class in com.here.sdk.core.engine">AuthenticationMode</a> authenticationMode)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs a SDKOptions from authentication mode.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>

<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#hashCode()">hashCode</a>()</code></div>

</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">

<ul class="member-list">
<li>
<section class="detail" id="scope">
<h3>scope</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">scope</span></div>
<div class="block"><p>Optional project ID to set the project scope of the login session. Not used if empty.
 see also <a href="https://www.here.com/docs/bundle/identity-and-access-management-developer-guide/page/topics/manage-projects.html">Manage Projects</a>
 and <a href="https://www.here.com/docs/bundle/identity-and-access-management-developer-guide/page/topics/concepts.html">IAM Concepts</a></p></div>
</section>
</li>
<li>
<section class="detail" id="cachePath">
<h3>cachePath</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">cachePath</span></div>
<div class="block"><p>Path to be used for caching purposes. It should be a path to the desired location where the application has read/write permissions.
 The path can be on internal or external storage.
 By default, this returns an empty string. Setting a new string, will overwrite the internally used default paths:
 <code>Context.getCacheDir().getPath()</code>
 .
 If an absolute path is set, it will be used instead.
 If a relative path is set then directory <code>Context.getCacheDir().getPath()</code>
 is used as parent path.
 Note, The cache path should be located
 under <a href="https://developer.android.com/training/data-storage/app-specific">app-specific directory</a>.
 Using shared directories such as <code>Documents</code> is not recommended as it will expose HERE SDK files to the other apps.
 It will also require additional permissions such as <code>MANAGE_EXTERNAL_STORAGE</code> and results in a poorer HERE SDK performance overall.
 The recommended location in terms of file I/O speed is the app's internal storage directory, whereas an external SD card is expected to be slower.
 This also depends on the quality of the used SD card.</p></div>
</section>
</li>
<li>
<section class="detail" id="cacheSizeInBytes">
<h3>cacheSizeInBytes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">cacheSizeInBytes</span></div>
<div class="block"><p>Desired upper bound of application size in bytes. When cached data exceeds cache_size, least recently used data will be removed.
 Default value 256MB</p></div>
</section>
</li>
<li>
<section class="detail" id="dataPath">
<h3>dataPath</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">dataPath</span></div>
<div class="block"><p>Path used for storing application internal data, such as the offline search index and other essential data required for proper functionality.
 <strong>Note:</strong> For common use cases, prefer <a href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#persistentMapStoragePath"><code>persistentMapStoragePath</code></a>, or keep the default paths. Use <code>dataPath</code> only as a fallback if <a href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#persistentMapStoragePath"><code>persistentMapStoragePath</code></a> is not writable, for example, when you have an agreement with HERE to flash data at factory time.
 By default, this returns an empty string. In this case, the same path as <a href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#persistentMapStoragePath"><code>persistentMapStoragePath</code></a> will be used.
 If an absolute path is set, it will be used instead.
 If a relative path is set then directory <code>Context.getFilesDir().getPath()</code>
 is used as parent path.
 Application must have read/write permissions to the given desired path.
 It is recommended that the application has exclusive access to this path.
 Avoid using shared or public directories such as <code>Download</code> or <code>Documents</code>.
 Using such directories may cause certain HERE SDK features to behave with limitations.
 For example, index creation for offline search may fail or not function as expected.
 It is recommended not to use the application cache paths like <code>Context.getCacheDir().getPath()</code>
 , since operating system manages data in this location
 and data can be deleted if the device is low on storage space, which will result in application malfunction.
 The path can be on internal or external storage. The internal storage is recommended due to the file I/O speed.
 Note:
 If the <a href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#persistentMapStoragePath"><code>persistentMapStoragePath</code></a> is writable, <code>dataPath</code> can be left empty.
 If the <a href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#persistentMapStoragePath"><code>persistentMapStoragePath</code></a> is not writable, <code>dataPath</code> must be set and also be writable. Note that <code>dataPath</code> is used to store essential HERE SDK data.
 <strong>Important:</strong>
 There is no automatic migration of stored data between the <a href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#persistentMapStoragePath"><code>persistentMapStoragePath</code></a> and the <code>dataPath</code>. For ease of management,
 it's recommended to set the persistence path as writable and ignore <code>dataPath</code>.
 If <code>dataPath</code> is set differently from the <a href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#persistentMapStoragePath"><code>persistentMapStoragePath</code></a>, some data that would typically be saved in the <a href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#persistentMapStoragePath"><code>persistentMapStoragePath</code></a> will now be saved to <code>dataPath</code>.
 If <code>dataPath</code> is set and later unset, any data stored there will remain inaccessible and will not be migrated back.</p></div>
</section>
</li>
<li>
<section class="detail" id="persistentMapStoragePath">
<h3>persistentMapStoragePath</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">persistentMapStoragePath</span></div>
<div class="block"><p>Path to store persistent map data. This should be the a path to the desired location for which the application has read/write permissions.
 The path can be on internal or external storage.
 By default, this returns an empty string. Setting a new string, will overwrite the internally used default paths:
 <code>Context.getFilesDir().getPath()</code>
 .
 If an absolute path is set, it will be used instead.
 If a relative path is set then directory <code>Context.getFilesDir().getPath()</code>
 is used as parent path.
 <strong>Note</strong>: Offline maps stored at <code>&lt;persistent_map_storage_path&gt;/v1/&lt;access_key_id&gt;/ocm-map/</code>, where <code>&lt;access_key_id&gt;</code> is
 taken from <code>SDKOptions.authenticationMode</code>.
 When <code>SDKOptions</code> initialized with <code>AuthenticationMode.withToken</code> or <code>AuthenticationMode.withExternal</code>, then <code>&lt;access_key_id&gt;</code> left empty.
 Note, persistent map storage path should be located
 under <a href="https://developer.android.com/training/data-storage/app-specific">app-specific directory</a>.
 Using shared directories such as <code>Documents</code> is not recommended as it will expose HERE SDK files to the other apps.
 It will also require additional permissions such as <code>MANAGE_EXTERNAL_STORAGE</code> and results in a poorer HERE SDK performance overall.
 Additionally, the Android MediaProvider imposes certain restrictions on the creation of non-media files (such as temporary files or database files),
 which may cause some functionality to not behave as expected.
 The recommended location in terms of file I/O speed is the app's internal storage directory, whereas an external SD card is expected to be slower.
 This also depends on the quality of the used SD card.
 Note: If the persistent map storage location has the read only permission, then the <a href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions#dataPath"><code>dataPath</code></a> must be configured.</p></div>
</section>
</li>
<li>
<section class="detail" id="politicalView">
<h3>politicalView</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">politicalView</span></div>
<div class="block"><p>Geopolitical view of a country, defined as a three letter country code by ISO 3166-1 alpha-3. Each disputed territory has
 an international and an alternative geopolitical view.
 When set, the map view will show all country boundaries according to the geopolitical view of the country that has been set.
 Note: Defaults to an empty string which enables the international view.
 This is a beta feature and thus there can be bugs and unexpected behavior.</p></div>
</section>
</li>
<li>
<section class="detail" id="offlineMode">
<h3>offlineMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">offlineMode</span></div>
<div class="block"><p>Sets offline mode for the HERE SDK. Defaults to <code>false</code>. When enabled, this prevents the
 HERE SDK from initiating any online connection from starting.
 The mode can be disabled or enabled again at any time via <a href="sdk-for-android-explore-sdknativeengine#isOfflineMode()"><code>SDKNativeEngine.isOfflineMode()</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="layerConfiguration">
<h3>layerConfiguration</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration" title="class in com.here.sdk.core.engine">LayerConfiguration</a></span> <span class="element-name">layerConfiguration</span></div>
<div class="block"><p>Defines a list of data features that can be enabled / disabled. Once set to <a href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions" title="class in com.here.sdk.core.engine"><code>SDKOptions</code></a> when
 a new HERE SDK is constructed, it will affect the map cache and offline maps.
 When disabling certain features, less data will be prefetched when the map is rendered. Map
 data that was already cached will not be removed until the least recently used strategy (LRU)
 applies. That means you cannot remove any content from the map cache by updating the
 <a href="sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration" title="class in com.here.sdk.core.engine"><code>LayerConfiguration</code></a>. However, for new map data, it will be applied.
 For offline maps, this <a href="sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration" title="class in com.here.sdk.core.engine"><code>LayerConfiguration</code></a> can reduce the download size of all regions.
 Note that the <a href="sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration" title="class in com.here.sdk.core.engine"><code>LayerConfiguration</code></a> is applied globally to all regions that will be downloaded
 in the future. It will not affect already downloaded regions. Updating a region will also
 not update the <a href="sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration" title="class in com.here.sdk.core.engine"><code>LayerConfiguration</code></a>. Only the <a href="sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration" title="class in com.here.sdk.core.engine"><code>LayerConfiguration</code></a> will be used that was set
 globally when a region was downloaded for the first time. If you want to update the
 <a href="sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration" title="class in com.here.sdk.core.engine"><code>LayerConfiguration</code></a> for an already downloaded region, please delete the region and download it again.
 Please also note
 <ul>
<li>The <a href="sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration" title="class in com.here.sdk.core.engine"><code>LayerConfiguration</code></a> is only applicable for the HERE SDK (Navigate) that contains the offline maps
 feature. It has no effect on other licenses.</li>
<li>The <a href="sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration" title="class in com.here.sdk.core.engine"><code>LayerConfiguration</code></a> cannot be set separately for a region, it will be applied globally
 for all regions that will be downloaded in the future.</li>
<li>It is not possible to specify a separate <a href="sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration" title="class in com.here.sdk.core.engine"><code>LayerConfiguration</code></a> for the map cache and offline maps.
 The <a href="sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration" title="class in com.here.sdk.core.engine"><code>LayerConfiguration</code></a> will be always applied to both.</li>
<li>The <a href="sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration" title="class in com.here.sdk.core.engine"><code>LayerConfiguration</code></a> does affect the map cache when a device has connectivity. Even
 when a device has connectivity it will only download the specified layers.</li>
<li>This is a beta feature and thus there can be bugs and unexpected behavior.</li>
</ul></p></div>
</section>
</li>
<li>
<section class="detail" id="catalogConfigurations">
<h3>catalogConfigurations</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-com-here-sdk-core-engine-catalogconfiguration" title="class in com.here.sdk.core.engine">CatalogConfiguration</a>&gt;</span> <span class="element-name">catalogConfigurations</span></div>
<div class="block"><p>This field specifies how the <a href="sdk-for-android-explore-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a> should access, use and store
 data for different catalogs. You can access default catalogs on the HERE platform and
 also custom catalogs such as for self-hosted or BYOD (bring your own data) use cases.
 For further information about catalogs and related concepts see
 <a href="sdk-for-android-explore-com-here-sdk-core-engine-catalogconfiguration" title="class in com.here.sdk.core.engine"><code>CatalogConfiguration</code></a>
<strong>Note:</strong>
 This API is only available for the Navigate license. It has no affect on other license.</p></div>
</section>
</li>
<li>
<section class="detail" id="autoUpdateOfOnlineCache">
<h3>autoUpdateOfOnlineCache</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">autoUpdateOfOnlineCache</span></div>
<div class="block"><p>Parameter to enable automatic cache updates.
 When it is false, the cache will always use the same map version as
 offline maps. If offline maps are updated, the cache will be also updated.
 The cache version will never be older than the offline maps version.
 When it is true, the cache will be automatically updated to use the latest map data
 that is available. In that case, the cache may contain map data that is newer than
 the offline maps data. Note that auto updates may also lead to increased network traffic, as
 the cached data will be evicted tile-by-tile before it is filled with newer map data. This
 process continues everytime the user views a new map view area until the data is replaced.
 Once also the offline map data is updated by the user, both map versions will
 be the same again.
 If the value is also specified via the manifest (Android) or plist (iOS), than the
 value set via <code>SDKOptions</code> will overrule the value that was set in manifest/plist - until
 the current session ends and the value is read/set again.
 Note that offline maps are only available for the Navigate license.
 Defaults to <code>false</code>.
 <strong>Note:</strong> Do not use this yet, the behavior of this feature may be inconsistent.
 Once it will be usable, it will be announced in the regular HERE SDK release notes.</p></div>
</section>
</li>
<li>
<section class="detail" id="customEngineOptions">
<h3>customEngineOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="sdk-for-android-explore-com-here-sdk-core-engine-enginebaseurl" title="enum class in com.here.sdk.core.engine">EngineBaseURL</a>,<wbr/><a href="sdk-for-android-explore-com-here-sdk-core-engine-engineoptions" title="class in com.here.sdk.core.engine">EngineOptions</a>&gt;</span> <span class="element-name">customEngineOptions</span></div>
<div class="block"><p>Set custom options for SDK Engines. This includes:
 <ul>
<li><code>custom_base_url</code>: Allows engines to use custom base URLs for alternative services.
 By default, the available endpoints use HERE backend endpoints.
 If unsupported base URLs are specified, the related features will become non-functional.
 Please contact your HERE representative to learn about possible custom base URL usage options.</li>
<li><code>custom_authentication_mode</code>: Enables bearer authentication mode for engines,
 which adds or omits the header ("Authorization", "Bearer $Token") to each
 online request made by the module the object is added to.
 The token (if used) can be provided directly or retrieved via key/secret
 from a dedicated backend.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</li>
</ul></p></div>
</section>
</li>
<li>
<section class="detail" id="actionOnCacheLock">
<h3>actionOnCacheLock</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-core-engine-sdkoptions.actiononcachelock" title="enum class in com.here.sdk.core.engine">SDKOptions.ActionOnCacheLock</a></span> <span class="element-name">actionOnCacheLock</span></div>
<div class="block"><p>Specifies action to perform when cache folder is locked by another process. Default value is <a href="sdk-for-android-explore-sdkoptions.actiononcachelock#WAIT_LOCKING_APP_FINISH"><code>SDKOptions.ActionOnCacheLock.WAIT_LOCKING_APP_FINISH</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="authenticationMode">
<h3>authenticationMode</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-core-engine-authenticationmode" title="class in com.here.sdk.core.engine">AuthenticationMode</a></span> <span class="element-name">authenticationMode</span></div>
<div class="block"><p>Encapsulates Authentication method and parameters.</p></div>
</section>
</li>
<li>
<section class="detail" id="networkSettings">
<h3>networkSettings</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-core-engine-networksettings" title="class in com.here.sdk.core.engine">NetworkSettings</a></span> <span class="element-name">networkSettings</span></div>
<div class="block"><p>Network settings to use at the start. Some of those settings can be changed later.</p></div>
</section>
</li>
<li>
<section class="detail" id="lowMemoryMode">
<h3>lowMemoryMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">lowMemoryMode</span></div>
<div class="block"><p>If an application runs in a memory-constrained environment, enable this option to reduce the HERE SDK's memory footprint.
 When set to <code>true</code> configures internal memory caches to consume less memory.
 Reduction in cache sizes also reduces performance of the HERE SDK.
 In order to release memory occupied by internal caches see <a href="sdk-for-android-explore-sdknativeengine#purgeMemoryCaches(com.here.sdk.core.engine.SDKNativeEngine.PurgeMemoryStrategy)"><code>SDKNativeEngine.purgeMemoryCaches(com.here.sdk.core.engine.SDKNativeEngine.PurgeMemoryStrategy)</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="billingTag">
<h3>billingTag</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">billingTag</span></div>
<div class="block"><p>Internal to HERE SDK. DO NOT USE THIS YET.
 <strong>Warning:</strong> This is a placeholder and under developement. We will announce its availability in our changelog once it is ready for use.
 A parameter to set a billing tag to track your HERE platform usage across the various HERE services your application may contact.
 For more information on the billing tag, see our
 <a href="https://www.here.com/docs/bundle/cost-management-developer-guide/page/topics/tutorial-billing-tags.html">cost management guide</a>.
 The tag needs to follow the format as described in the guide or it will be ignored.
 The parameter defaults to <code>null</code>, which also means that the tag is ignored for all requests.
 <strong>Note:</strong> The billing tag is optional, but when set, it can help you to understand
 how often your app uses certain services, for example, the number of hits to our
 HERE backend routing services. For more details on tracking such details,
 please consult the <em>cost management guide</em> or get in touch with the HERE billing team.</p></div>
</section>
</li>
<li>
<section class="detail" id="customOptions">
<h3>customOptions</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-core-metadata" title="class in com.here.sdk.core">Metadata</a></span> <span class="element-name">customOptions</span></div>
<div class="block"><p>Options that define custom behavior for the HERE SDK. These settings allow fine-tuning
 of internal thread pools and resource management for advanced use cases.
 These options are intended for <em>internal</em> usage only and should not be modified unless
 instructed by HERE support.
 Note: This is a <em>beta</em> release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.engine.AuthenticationMode)">
<h3>SDKOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SDKOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-com-here-sdk-core-engine-authenticationmode" title="class in com.here.sdk.core.engine">AuthenticationMode</a> authenticationMode)</span></div>
<div class="block"><p>Constructs a SDKOptions from authentication mode. Other fields are filled with default values.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>authenticationMode</code> - <p>Authentication Mode used for obtaining an access token.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hashCode()">
<h3>hashCode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->






</div>
`
}</HTMLBlock>
