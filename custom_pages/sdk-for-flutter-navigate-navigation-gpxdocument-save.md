---
title: "save method - GPXDocument class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-gpxdocument-save"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- save.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/GPXDocument-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">save</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">bool</span> <span class="name">save</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-save-param-gpxFilePath" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">gpxFilePath</span></span>

)

</div>

<div class="section desc markdown">

Saves the document to a file.

For saving the <a href="sdk-for-flutter-navigate-navigation-gpxdocument-tracks">GPXDocument.tracks</a> modification before writing to a file, use <a href="sdk-for-flutter-navigate-navigation-gpxtrackwriter-class">GPXTrackWriter</a>.

- `gpxFilePath` The file path where the GPX document will be saved.

Returns `bool`. `True` if the document has been saved successfully. `False` if an error has been happened during saving.

</div>

## Implementation

``` dart
bool save(String gpxFilePath);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
