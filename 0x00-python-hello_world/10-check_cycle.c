#include "lists.h"

/**
 * check_cycle - function that check if the sigle linked list is cycle
 *
 * @list: the linked list to check
 *
 * Return: 1 if there a cycle and 0 if no
*/

int check_cycle(listint_t *list)
{
	listint_t *low = list, *high = list;

	while (high && high->next)
	{
		low = low->next;
		high = high->next->next;
		if (low == high)
			return (1);
	}
	return (0);
}
