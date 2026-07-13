---
title: "onPostActions method - PostActionListener class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-postactionlistener-onpostactions"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/PostActionListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">onPostActions</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">onPostActions</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-onPostActions-param-postActions" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-postaction-class">PostAction</a></span>\></span></span> <span class="parameter-name">postActions</span></span>

)

</div>

<div class="section desc markdown">

Called whenever <a href="sdk-for-flutter-navigate-routing-postaction-class">PostAction</a>'s are available.

Note that <a href="sdk-for-flutter-navigate-routing-postaction-class">PostAction</a>'s are performed after the arrival at the end of a section.

- `postActions` The post actions that should be performed.

</div>

## Implementation

``` dart
void onPostActions(List<PostAction> postActions);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

