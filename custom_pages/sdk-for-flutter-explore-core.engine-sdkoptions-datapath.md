---
title: "dataPath property - SDKOptions class - core.engine library - Dart API"
slug: "sdk-for-flutter-explore-core.engine-sdkoptions-datapath"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- dataPath.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/SDKOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">dataPath</span> property

</div>

<div class="section multi-line-signature">

String <span class="name">dataPath</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Path used for storing application internal data, such as the offline search index and other essential data required for proper functionality.

**Note:** For common use cases, prefer <a href="sdk-for-flutter-explore-core-engine-sdkoptions-persistentmapstoragepath">SDKOptions.persistentMapStoragePath</a>, or keep the default paths. Use `dataPath` only as a fallback if <a href="sdk-for-flutter-explore-core-engine-sdkoptions-persistentmapstoragepath">SDKOptions.persistentMapStoragePath</a> is not writable, for example, when you have an agreement with HERE to flash data at factory time.

By default, this returns an empty string. In this case, the same path as <a href="sdk-for-flutter-explore-core-engine-sdkoptions-persistentmapstoragepath">SDKOptions.persistentMapStoragePath</a> will be used. If an absolute path is set, it will be used instead. If a relative path is set then directory `Application Library directory` for iOS and

    Context.getFilesDir().getPath()

for Android is used as parent path. Application must have read/write permissions to the given desired path. It is recommended that the application has exclusive access to this path. Avoid using shared or public directories such as `Download` or `Documents`. Using such directories may cause certain HERE SDK features to behave with limitations. For example, index creation for offline search may fail or not function as expected. It is recommended not to use the application cache paths like `<Application_Home>/Library/Caches` for iOS and

    Context.getCacheDir().getPath()

for Android, since operating system manages data in this location and data can be deleted if the device is low on storage space, which will result in application malfunction. The path can be on internal or external storage. The internal storage is recommended due to the file I/O speed. Note: If the <a href="sdk-for-flutter-explore-core-engine-sdkoptions-persistentmapstoragepath">SDKOptions.persistentMapStoragePath</a> is writable, `dataPath` can be left empty. If the <a href="sdk-for-flutter-explore-core-engine-sdkoptions-persistentmapstoragepath">SDKOptions.persistentMapStoragePath</a> is not writable, `dataPath` must be set and also be writable. Note that `dataPath` is used to store essential HERE SDK data.
</p>

**Important:** There is no automatic migration of stored data between the <a href="sdk-for-flutter-explore-core-engine-sdkoptions-persistentmapstoragepath">SDKOptions.persistentMapStoragePath</a> and the `dataPath`. For ease of management, it's recommended to set the persistence path as writable and ignore `dataPath`. If `dataPath` is set differently from the <a href="sdk-for-flutter-explore-core-engine-sdkoptions-persistentmapstoragepath">SDKOptions.persistentMapStoragePath</a>, some data that would typically be saved in the <a href="sdk-for-flutter-explore-core-engine-sdkoptions-persistentmapstoragepath">SDKOptions.persistentMapStoragePath</a> will now be saved to `dataPath`. If `dataPath` is set and later unset, any data stored there will remain inaccessible and will not be migrated back.

</div>

## Implementation

``` dart
String dataPath;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
