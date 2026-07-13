---
title: "VisualNavigator.withNavigator constructor - VisualNavigator - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-visualnavigator-visualnavigator-withnavigator"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- VisualNavigator.withNavigator.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/VisualNavigator-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">VisualNavigator.withNavigator</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">VisualNavigator.withNavigator</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-withNavigator-param-navigator" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-class">NavigatorInterface</a></span> <span class="parameter-name">navigator</span></span>

)

</div>

<div class="section desc markdown">

Creates a new instance of this class using provided instance of <a href="sdk-for-flutter-navigate-navigation-navigatorinterface-class">NavigatorInterface</a> as source of data.

**Note:** The <a href="sdk-for-flutter-navigate-navigation-visualnavigator-class">VisualNavigator</a> implements the <a href="sdk-for-flutter-navigate-navigation-navigatorinterface-class">NavigatorInterface</a> interface and forwards all calls to the underlying <a href="sdk-for-flutter-navigate-navigation-navigatorinterface-class">NavigatorInterface</a> instance. When multiple <a href="sdk-for-flutter-navigate-navigation-visualnavigator-class">VisualNavigator</a> instances share the same <a href="sdk-for-flutter-navigate-navigation-navigatorinterface-class">NavigatorInterface</a> instance, method calls on this common instance will overwrite changes made by another, which may lead to unexpected behavior.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

- `navigator` A NavigatorInterface implementation instance.

Throws <a href="sdk-for-flutter-navigate-core-errors-instantiationexception-class">InstantiationException</a>. <a href="sdk-for-flutter-navigate-core-errors-instantiationexception-class">InstantiationException</a> when operation fails.

</div>

## Implementation

``` dart
factory VisualNavigator.withNavigator(NavigatorInterface navigator) => $prototype.withNavigator(navigator);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
