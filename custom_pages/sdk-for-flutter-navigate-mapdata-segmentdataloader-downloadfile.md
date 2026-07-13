---
title: "downloadFile method - SegmentDataLoader class - mapdata library - Dart API"
slug: "sdk-for-flutter-navigate-mapdata-segmentdataloader-downloadfile"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapdata/SegmentDataLoader-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">downloadFile</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">List<span class="signature">\<<wbr></wbr><span class="type-parameter">Uint8List</span>\></span></span> <span class="name">downloadFile</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-downloadFile-param-fileReferences" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-mapdata-filereference-class">FileReference</a></span>\></span></span> <span class="parameter-name">fileReferences</span>, </span>
2.  <span id="sdk-for-flutter-navigate-downloadFile-param-downloadingOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapdata-downloadingfileoptions-class">DownloadingFileOptions</a></span> <span class="parameter-name">downloadingOptions</span></span>

)

</div>

<div class="section desc markdown">

Synchronously load the optional image providing guidance of a directed or non directed segment.

- `fileReferences` Provides information for a file reference.

- `downloadingOptions` Provides information regarding downloading configuration.

Returns `List<Uint8List>`. Requested data of a segment.

Throws <a href="sdk-for-flutter-navigate-mapdata-mapdataloaderexceptionexception-class">MapDataLoaderExceptionException</a>. Specifies reason, why list of data of a segment is not returned.

</div>

## Implementation

``` dart
List<Uint8List> downloadFile(List<FileReference> fileReferences, DownloadingFileOptions downloadingOptions);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

