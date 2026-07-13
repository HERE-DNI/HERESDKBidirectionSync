---
title: "RepairPersistentMapCallback typedef - maploader library - Dart API"
slug: "sdk-for-flutter-navigate-maploader-repairpersistentmapcallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RepairPersistentMapCallback.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader/maploader-library-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-typedef">RepairPersistentMapCallback</span> typedef

</div>

<div class="section multi-line-signature">

<span class="name">RepairPersistentMapCallback</span> = <span class="returntype">void Function<span class="signature">(<span id="sdk-for-flutter-navigate-param-persistentMapRepairError" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-persistentmaprepairerror">PersistentMapRepairError</a>?</span> <span class="parameter-name">persistentMapRepairError</span></span>)</span></span>

</div>

<div class="section desc markdown">

A method which is called on the main thread when <a href="sdk-for-flutter-navigate-maploader-mapdownloader-repairpersistentmap">MapDownloader.repairPersistentMap</a> has been completed.

The first argument indicates an error in case of a failure. The second argument contains the results. Both arguments cannot be `null` at the same time - or not `null` at the same time.

- `persistentMapRepairError` Represents an error in case of a failure. It is `null` for an operation that succeeds.

</div>

## Implementation

``` dart
typedef RepairPersistentMapCallback = void Function(PersistentMapRepairError? persistentMapRepairError);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
