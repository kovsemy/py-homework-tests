### Дополнение
**recycle_pokemonbattle** - криво-косо исполненная автоматизация процесса драки между покемонами, чтобы не пользоваться коллекциями в Postman, у которых всего 25 запросов... можно реализовать такую вот относительно простую логику.

```sh
Моменты:
1. Нет проверки покемона на покеболл, поэтому если руками создать покемона, руками его и в покеболл добавить нужно, а программа сама проверяет есть ли у нас вообще покемоны для битв, если нет - создает.
2. Поиск соперника идет по принципу "2 <= атака врага <= наша атака", не самая лучшая тактика поиска врагов, но улучшение этого всего дело подождет..
3. Мы будем искать врага до тех пор, пока не закончится список врагов, либо мы не найдем подходящего. Если победим, снова идем искать врага, проиграем - проиграем.. А если в списке покемонов в покеболле не найдем никого хотя бы чуточку равного нам, просто не будем ни с кем драться:)
4. Нет никакой обработки на ограничение по битвам, почему? Да пошел гулять на улицу и не сделал, а потом уже и домашку надо сдавать))
5. В целом вполне себе ок, всего лишь нужно нажать одну кнопочку и у нас уже пошел жесткий кач)
```