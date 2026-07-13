---
title: "setAccessKeySecret method - SDKNativeEngine class - core.engine library - Dart API"
slug: "sdk-for-flutter-explore-core.engine-sdknativeengine-setaccesskeysecret"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setAccessKeySecret.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/SDKNativeEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">setAccessKeySecret</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">setAccessKeySecret</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-setAccessKeySecret-param-accessKeySecret" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">accessKeySecret</span></span>

)

</div>

<div class="section desc markdown">

Overrides HERE SDK access key secret with new value.

The new credentials will be used for new requests.

**Note:** This method can be called from any thread. Access key ID can be set with constructor of SDKNativeEngine. New instance of SDKNativeEngine should be used if a new access key ID is required.

- `accessKeySecret` New access key secret.

</div>

## Implementation

``` dart
void setAccessKeySecret(String accessKeySecret);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
