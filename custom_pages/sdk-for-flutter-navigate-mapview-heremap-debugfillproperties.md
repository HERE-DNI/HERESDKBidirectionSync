---
title: "debugFillProperties method - HereMap class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-heremap-debugfillproperties"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/HereMap-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">debugFillProperties</span> method

</div>

<div class="section multi-line-signature">

<div>

1.  @override

</div>

<span class="returntype">void</span> <span class="name">debugFillProperties</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-debugFillProperties-param-properties" class="parameter"><span class="type-annotation">DiagnosticPropertiesBuilder</span> <span class="parameter-name">properties</span></span>

)

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<div class="section desc markdown">

Add additional properties associated with the node.

<iframe allow="accelerometer; 
autoplay; 
clipboard-write; 
encrypted-media; 
gyroscope; 
picture-in-picture" allowfullscreen frameborder="0" src="https://www.youtube.com/embed/DnC7eT-vh1k?rel=0" style="max-width: 560px;
max-height: 315px;
width: 100%;
height: 100%;
aspect-ratio: 560 / 315;" title="YouTube video player">

</iframe>

Use the most specific `DiagnosticsProperty` existing subclass to describe each property instead of the `DiagnosticsProperty` base class. There are only a small number of `DiagnosticsProperty` subclasses each covering a common use case. Consider what values a property is relevant for users debugging as users debugging large trees are overloaded with information. Common named parameters in `DiagnosticsNode` subclasses help filter when and how properties are displayed.

`defaultValue`, `showName`, `showSeparator`, and `level` keep string representations of diagnostics terse and hide properties when they are not very useful.

- Use `defaultValue` any time the default value of a property is uninteresting. For example, specify a default value of null any time a property being null does not indicate an error.

- Avoid specifying the `level` parameter unless the result you want cannot be achieved by using the `defaultValue` parameter or using the `ObjectFlagProperty` class to conditionally display the property as a flag.

- Specify `showName` and `showSeparator` in rare cases where the string output would look clumsy if they were not set.

  ``` dart
  DiagnosticsProperty<Object>('child(3, 4)', null, ifNull: 'is null', showSeparator: false).toString()
  ```

  </pre>

  Shows using `showSeparator` to get output

      child(3, 4) is null

  which is more polished than

      child(3, 4): is null

  .

  ``` dart
  DiagnosticsProperty<IconData>('icon', icon, ifNull: '<empty>', showName: false).toString()
  ```

  </pre>

  Shows using `showName` to omit the property name as in this context the property name does not add useful information.

`ifNull`, `ifEmpty`, `unit`, and `tooltip` make property descriptions clearer. The examples in the code sample below illustrate good uses of all of these parameters.

## DiagnosticsProperty subclasses for primitive types

- `StringProperty`, which supports automatically enclosing a `String` value in quotes.
- `DoubleProperty`, which supports specifying a unit of measurement for a `double` value.
- `PercentProperty`, which clamps a `double` to between 0 and 1 and formats it as a percentage.
- `IntProperty`, which supports specifying a unit of measurement for an `int` value.
- `FlagProperty`, which formats a `bool` value as one or more flags. Depending on the use case it is better to format a bool as `DiagnosticsProperty<bool>` instead of using `FlagProperty` as the output is more verbose but unambiguous.

## Other important `DiagnosticsProperty` variants

- `EnumProperty`, which provides terse descriptions of enum values working around limitations of the `toString` implementation for Dart enum types.
- `IterableProperty`, which handles iterable values with display customizable depending on the `DiagnosticsTreeStyle` used.
- `ObjectFlagProperty`, which provides terse descriptions of whether a property value is present or not. For example, whether an `onClick` callback is specified or an animation is in progress.
- `ColorProperty`, which must be used if the property value is a `Color` or one of its subclasses.
- `IconDataProperty`, which must be used if the property value is of type `IconData`.

If none of these subclasses apply, use the `DiagnosticsProperty` constructor or in rare cases create your own `DiagnosticsProperty` subclass as in the case for `TransformProperty` which handles <a href="https://pub.dev/documentation/vector_math/2.2.0/vector_math_64/Matrix4-class.html">Matrix4</a> that represent transforms. Generally any property value with a good `toString` method implementation works fine using `DiagnosticsProperty` directly.

{@tool snippet}

This example shows best practices for implementing <a href="sdk-for-flutter-navigate-mapview-heremap-debugfillproperties">debugFillProperties</a> illustrating use of all common `DiagnosticsProperty` subclasses and all common `DiagnosticsProperty` parameters.

``` dart
class ExampleObject extends ExampleSuperclass {

  // ...various members and properties...

  @override
  void debugFillProperties(DiagnosticPropertiesBuilder properties) {
    // Always add properties from the base class first.
    super.debugFillProperties(properties);

    // Omit the property name 'message' when displaying this String property
    // as it would just add visual noise.
    properties.add(StringProperty('message', message, showName: false));

    properties.add(DoubleProperty('stepWidth', stepWidth));

    // A scale of 1.0 does nothing so should be hidden.
    properties.add(DoubleProperty('scale', scale, defaultValue: 1.0));

    // If the hitTestExtent matches the paintExtent, it is just set to its
    // default value so is not relevant.
    properties.add(DoubleProperty('hitTestExtent', hitTestExtent, defaultValue: paintExtent));

    // maxWidth of double.infinity indicates the width is unconstrained and
    // so maxWidth has no impact.
    properties.add(DoubleProperty('maxWidth', maxWidth, defaultValue: double.infinity));

    // Progress is a value between 0 and 1 or null. Showing it as a
    // percentage makes the meaning clear enough that the name can be
    // hidden.
    properties.add(PercentProperty(
      'progress',
      progress,
      showName: false,
      ifNull: '<indeterminate>',
    ));

    // Most text fields have maxLines set to 1.
    properties.add(IntProperty('maxLines', maxLines, defaultValue: 1));

    // Specify the unit as otherwise it would be unclear that time is in
    // milliseconds.
    properties.add(IntProperty('duration', duration.inMilliseconds, unit: 'ms'));

    // Tooltip is used instead of unit for this case as a unit should be a
    // terse description appropriate to display directly after a number
    // without a space.
    properties.add(DoubleProperty(
      'device pixel ratio',
      devicePixelRatio,
      tooltip: 'physical pixels per logical pixel',
    ));

    // Displaying the depth value would be distracting. Instead only display
    // if the depth value is missing.
    properties.add(ObjectFlagProperty<int>('depth', depth, ifNull: 'no depth'));

    // bool flag that is only shown when the value is true.
    properties.add(FlagProperty('using primary controller', value: primary));

    properties.add(FlagProperty(
      'isCurrent',
      value: isCurrent,
      ifTrue: 'active',
      ifFalse: 'inactive',
    ));

    properties.add(DiagnosticsProperty<bool>('keepAlive', keepAlive));

    // FlagProperty could have also been used in this case.
    // This option results in the text "obscureText: true" instead
    // of "obscureText" which is a bit more verbose but a bit clearer.
    properties.add(DiagnosticsProperty<bool>('obscureText', obscureText, defaultValue: false));

    properties.add(EnumProperty<TextAlign>('textAlign', textAlign, defaultValue: null));
    properties.add(EnumProperty<ImageRepeat>('repeat', repeat, defaultValue: ImageRepeat.noRepeat));

    // Warn users when the widget is missing but do not show the value.
    properties.add(ObjectFlagProperty<Widget>('widget', widget, ifNull: 'no widget'));

    properties.add(IterableProperty<BoxShadow>(
      'boxShadow',
      boxShadow,
      defaultValue: null,
      style: style,
    ));

    // Getting the value of size throws an exception unless hasSize is true.
    properties.add(DiagnosticsProperty<Size>.lazy(
      'size',
      () => size,
      description: '${ hasSize ? size : "MISSING" }',
    ));

    // If the `toString` method for the property value does not provide a
    // good terse description, write a DiagnosticsProperty subclass as in
    // the case of TransformProperty which displays a nice debugging view
    // of a Matrix4 that represents a transform.
    properties.add(TransformProperty('transform', transform));

    // If the value class has a good `toString` method, use
    // DiagnosticsProperty<YourValueType>. Specifying the value type ensures
    // that debugging tools always know the type of the field and so can
    // provide the right UI affordances. For example, in this case even
    // if color is null, a debugging tool still knows the value is a Color
    // and can display relevant color related UI.
    properties.add(DiagnosticsProperty<Color>('color', color));

    // Use a custom description to generate a more terse summary than the
    // `toString` method on the map class.
    properties.add(DiagnosticsProperty<Map<Listenable, VoidCallback>>(
      'handles',
      handles,
      description: handles != null
        ? '${handles!.length} active client${ handles!.length == 1 ? "" : "s" }'
        : null,
      ifNull: 'no notifications ever received',
      showName: false,
    ));
  }
}
```

</pre>

{@end-tool}

Used by <a href="sdk-for-flutter-navigate-mapview-heremap-todiagnosticsnode">toDiagnosticsNode</a> and <a href="sdk-for-flutter-navigate-mapview-heremap-tostring">toString</a>.

Do not add values that have lifetime shorter than the object.

</div>

## Implementation

``` dart
@override
void debugFillProperties(DiagnosticPropertiesBuilder properties) {
  super.debugFillProperties(properties);
  properties.defaultDiagnosticsTreeStyle = DiagnosticsTreeStyle.dense;
}
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

