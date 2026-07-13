---
title: "persistentMapStoragePath property - SDKOptions class - core.engine library - Dart API"
slug: "sdk-for-flutter-explore-core.engine-sdkoptions-persistentmapstoragepath"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/SDKOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">persistentMapStoragePath</span> property

</div>

<div class="section multi-line-signature">

String <span class="name">persistentMapStoragePath</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Path to store persistent map data. This should be the a path to the desired location for which the application has read/write permissions. The path can be on internal or external storage. By default, this returns an empty string. Setting a new string, will overwrite the internally used default paths:

`Application Library directory` for iOS and

    Context.getFilesDir().getPath()

for Android. If an absolute path is set, it will be used instead. If a relative path is set then directory `Application Library directory` for iOS and

    Context.getFilesDir().getPath()

for Android is used as parent path. **Note**: Offline maps stored at `<persistent_map_storage_path>/v1/<access_key_id>/ocm-map/`, where `<access_key_id>` is taken from `SDKOptions.authenticationMode`. When `SDKOptions` initialized with `AuthenticationMode.withToken` or `AuthenticationMode.withExternal`, then `<access_key_id>` left empty.
</p>

Note: If the persistent map storage location has the read only permission, then the <a href="sdk-for-flutter-explore-core-engine-sdkoptions-datapath">SDKOptions.dataPath</a> must be configured.

</div>

## Implementation

``` dart
String persistentMapStoragePath;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

