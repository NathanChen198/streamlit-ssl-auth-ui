/*
author: Nathan Chen
date  : 12-Mar-2024
*/


export enum TextAlign{
  left = 'left',
  right = 'right',
  center = 'center',
  justify = 'justify',
  matchParent = 'match-parent'
}
export const getTextAlign = (align: any, defaultAlign: TextAlign = TextAlign.left) : TextAlign =>
  (typeof align === 'string') ? TextAlign[align as keyof typeof TextAlign] : defaultAlign


export enum TitleSize{
  small = 4,
  medium = 3,
  large = 2,
  extraLarge = 1
}
export const getTitleSize = (size: any, defaultSize: TitleSize = TitleSize.medium) : TitleSize => {
  if(typeof size === 'string')
    return TitleSize[size as keyof typeof TitleSize]
  else if(typeof size === 'number')
    return size
  else
    return defaultSize
}

export enum InputType{
  text = "text",
  number = "number",
  boolean = "boolean",
  color = "color",
  date = "date",
  time = "time",
  datetime = "datetime",
  date_range = "date_range",
  choose_one = "choose_one",
  choose_many = "choose_many",
}
export const getInputType = (type: any) : InputType | undefined => {
  if(typeof type === 'string')
    return InputType[type as keyof typeof InputType]
  else
    return undefined
}