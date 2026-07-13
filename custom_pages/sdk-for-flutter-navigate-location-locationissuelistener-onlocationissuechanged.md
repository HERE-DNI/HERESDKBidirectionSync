---
title: "onLocationIssueChanged method - LocationIssueListener class - location library - Dart API"
slug: "sdk-for-flutter-navigate-location-locationissuelistener-onlocationissuechanged"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="location/LocationIssueListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">onLocationIssueChanged</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">onLocationIssueChanged</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-onLocationIssueChanged-param-issues" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-location-locationissuetype">LocationIssueType</a></span>\></span></span> <span class="parameter-name">issues</span></span>

)

</div>

<div class="section desc markdown">

Called when the snapshot of currently active location issues changes.

Invoked whenever the LocationEngine detects a change in the set of active issues, including when all issues clear (empty list). Replace any previously stored issue list with this snapshot.

- `issues` Current snapshot of active location issues. Empty list indicates no active issues.

</div>

## Implementation

``` dart
void onLocationIssueChanged(List<LocationIssueType> issues);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

