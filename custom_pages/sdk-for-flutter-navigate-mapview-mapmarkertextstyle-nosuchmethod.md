---
title: "noSuchMethod method - MapMarkerTextStyle class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapmarkertextstyle-nosuchmethod"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapMarkerTextStyle-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">noSuchMethod</span> method

</div>

<div class="section multi-line-signature">

<span class="returntype">dynamic</span> <span class="name">noSuchMethod</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>

)

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<div class="section desc markdown">

Invoked when a nonexistent method or property is accessed.

A dynamic member invocation can attempt to call a member which doesn't exist on the receiving object. Example:

``` dart
dynamic object = 1;
object.add(42); // Statically allowed, run-time error
```

</pre>

This invalid code will invoke the `noSuchMethod` method of the integer `1` with an `Invocation` representing the

    .add(42)

call and arguments (which then throws).
</p>

Classes can override `noSuchMethod` to provide custom behavior for such invalid dynamic invocations.

A class with a non-default `noSuchMethod` invocation can also omit implementations for members of its interface. Example:

``` dart
class MockList<T> implements List<T> {
  noSuchMethod(Invocation invocation) {
    log(invocation);
    super.noSuchMethod(invocation); // Will throw.
  }
}
void main() {
  MockList().add(42);
}
```

</pre>

This code has no compile-time warnings or errors even though the `MockList` class has no concrete implementation of any of the `List` interface methods. Calls to `List` methods are forwarded to `noSuchMethod`, so this code will `log` an invocation similar to

    Invocation.method(#add, [42])

and then throw.
</p>

If a value is returned from `noSuchMethod`, it becomes the result of the original invocation. If the value is not of a type that can be returned by the original invocation, a type error occurs at the invocation.

The default behavior is to throw a `NoSuchMethodError`.

</div>

## Implementation

``` dart
@pragma("vm:entry-point")
@pragma("wasm:entry-point")
external dynamic noSuchMethod(Invocation invocation);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

