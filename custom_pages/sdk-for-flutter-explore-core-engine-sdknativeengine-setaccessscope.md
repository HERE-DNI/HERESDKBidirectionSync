---
title: "setAccessScope method - SDKNativeEngine class - core.engine library - Dart API"
slug: "sdk-for-flutter-explore-core-engine-sdknativeengine-setaccessscope"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/SDKNativeEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">setAccessScope</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">setAccessScope</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-setAccessScope-param-scope" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">scope</span></span>

)

</div>

<div class="section desc markdown">

Overrides the token scope of the HERE SDK with new value.

A new token will be fetched with the set scope and used for future requests. Setting an empty string will fetch a token for the global scope.

This method can be called from any thread.

- `scope` New scope for token

</div>

## Implementation

``` dart
void setAccessScope(String scope);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

